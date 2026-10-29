// connect.js
// Zero-dependency Node.js client to easily connect this dataset to any JavaScript/TypeScript/Node.js app.

const fs = require('fs');
const path = require('path');

const EXPORTS_FILE = path.join(__dirname, 'data', 'training_exports', 'all_domains_benchmark.jsonl');
const REGISTRY_FILE = path.join(__dirname, 'metadata', 'dataset_registry.jsonl');

class DatasetClient {
    constructor(dataPath = EXPORTS_FILE) {
        this.dataPath = dataPath;
        this.cache = null;
    }

    _loadData() {
        if (!this.cache) {
            this.cache = [];
            if (fs.existsSync(this.dataPath)) {
                const lines = fs.readFileSync(this.dataPath, 'utf-8').split('\n');
                for (const line of lines) {
                    if (line.trim()) {
                        try {
                            this.cache.push(jsonParseSafe(line));
                        } catch (e) {}
                    }
                }
            }
        }
        return this.cache;
    }

    listDomains() {
        const data = this._loadData();
        const set = new Set();
        data.forEach(r => { if (r.domain) set.add(r.domain); });
        return Array.from(set).sort();
    }

    listSubtopics(domainFilter = null) {
        const data = this._loadData();
        const map = new Map();
        data.forEach(r => {
            if (!domainFilter || r.domain.toLowerCase().includes(domainFilter.toLowerCase())) {
                const key = `${r.domain}::${r.subtopic}`;
                if (!map.has(key)) {
                    map.set(key, { domain: r.domain, subtopic: r.subtopic });
                }
            }
        });
        return Array.from(map.values());
    }

    get({ domain, subtopic, limit } = {}) {
        const data = this._loadData();
        const results = [];
        const dLower = domain ? domain.toLowerCase() : null;
        const sLower = subtopic ? subtopic.toLowerCase() : null;

        for (const r of data) {
            if (dLower && !r.domain.toLowerCase().includes(dLower) && !(r.domain_id && r.domain_id.toLowerCase().includes(dLower))) {
                continue;
            }
            if (sLower && !r.subtopic.toLowerCase().includes(sLower) && !(r.subtopic_id && r.subtopic_id.toLowerCase().includes(sLower))) {
                continue;
            }
            results.push(r);
            if (limit && results.length >= limit) break;
        }
        return results;
    }

    search(query, limit = 10) {
        const data = this._loadData();
        const tokens = (query || '').toLowerCase().match(/\w+/g) || [];
        if (!tokens.length) return [];

        const scored = [];
        for (const r of data) {
            const text = `${r.text || ''} ${r.domain || ''} ${r.subtopic || ''}`.toLowerCase();
            let score = 0;
            tokens.forEach(tok => {
                const matches = text.split(tok).length - 1;
                score += matches;
            });
            if (score > 0) scored.push({ score, record: r });
        }
        scored.sort((a, b) => b.score - a.score);
        return scored.slice(0, limit).map(s => s.record);
    }
}

function jsonParseSafe(str) {
    try {
        return JSON.parse(str);
    } catch (e) {
        return null;
    }
}

module.exports = { DatasetClient };

// Simple CLI test if run directly
if (require.main === module) {
    const client = new DatasetClient();
    console.log("=== Node.js Dataset Connector Test ===");
    const domains = client.listDomains();
    console.log(`Loaded ${domains.length} domains in JavaScript.`);
    const sample = client.get({ domain: "cricket", limit: 1 });
    if (sample.length) {
        console.log("Sample cricket record:", sample[0].title || sample[0].subtopic);
    }
}
