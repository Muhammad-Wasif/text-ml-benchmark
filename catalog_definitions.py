# catalog_definitions.py
# Complete verified 200-subtopic catalog definitions across 50 domains

CATALOG = [
    {
        "domain_id": "01_education_and_studying",
        "domain_name": "Education and studying",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "01_01",
        "subtopic_name": "Study techniques and learning strategies",
        "candidate_title": "Effective Study Strategies & Learning Techniques Knowledge Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Study_skills",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Study_skills|Active_recall|Spaced_repetition|Pomodoro_Technique&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "study_skills_and_strategies.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Encyclopedia synthesis",
            "Requires standard CC-BY-SA attribution"
        ]
    },
    {
        "domain_id": "01_education_and_studying",
        "domain_name": "Education and studying",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "01_02",
        "subtopic_name": "Exam preparation and revision",
        "candidate_title": "MMLU High School Examination & Revision Benchmark",
        "source_platform": "Hugging Face",
        "publisher": "Hugging Face Contributor Community",
        "source_url": "https://huggingface.co/datasets/cais/mmlu",
        "download_url": "https://datasets-server.huggingface.co/rows?dataset=cais%2Fmmlu&config=college_biology&split=test&offset=0&limit=100",
        "license": "MIT",
        "language": "en",
        "format": "json",
        "target_filename": "mmlu_college_biology_revision.json",
        "text_fields": [
            "question",
            "choices",
            "answer"
        ],
        "limitations": [
            "Multiple-choice examination format",
            "Restricted to biology slice"
        ]
    },
    {
        "domain_id": "01_education_and_studying",
        "domain_name": "Education and studying",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "01_03",
        "subtopic_name": "Student time management",
        "candidate_title": "Student Time Management and Academic Productivity Reference Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Time_management",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Time_management|Procrastination|Time_blocking|Work%E2%80%93life_balance&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "student_time_management_extracts.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Descriptive academic principles",
            "Qualitative conceptual text"
        ]
    },
    {
        "domain_id": "01_education_and_studying",
        "domain_name": "Education and studying",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "01_04",
        "subtopic_name": "Academic performance and study habits",
        "candidate_title": "Student Study Habits and Academic Performance Survey Dataset",
        "source_platform": "GitHub",
        "publisher": "GitHub Contributor Community",
        "source_url": "https://github.com/f111242256-dotcom/student-performance.csv-dataset",
        "download_url": "https://raw.githubusercontent.com/f111242256-dotcom/student-performance.csv-dataset/main/Student_Performance.csv",
        "license": "MIT",
        "language": "en",
        "format": "csv",
        "target_filename": "student_study_habits_performance.csv",
        "text_fields": [
            "Extracurricular Activities",
            "Sleep Hours",
            "Sample Question Papers Practiced"
        ],
        "limitations": [
            "Survey sample representation",
            "Mixed tabular and textual features"
        ]
    },
    {
        "domain_id": "02_general_knowledge",
        "domain_name": "General knowledge",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "02_01",
        "subtopic_name": "World geography",
        "candidate_title": "World Geography Countries and Territories Gazeteer Corpus",
        "source_platform": "GitHub",
        "publisher": "GitHub Contributor Community",
        "source_url": "https://github.com/mledoze/countries",
        "download_url": "https://raw.githubusercontent.com/mledoze/countries/master/countries.json",
        "license": "ODbL 1.0",
        "language": "en",
        "format": "json",
        "target_filename": "world_geography_countries_gazetteer.json",
        "text_fields": [
            "name",
            "capital",
            "region",
            "subregion"
        ],
        "limitations": [
            "Structured geo-entity database",
            "Political status per UN norms"
        ]
    },
    {
        "domain_id": "02_general_knowledge",
        "domain_name": "General knowledge",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "02_02",
        "subtopic_name": "Historical civilizations",
        "candidate_title": "Ancient Historical Civilizations Knowledge Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Cradle_of_civilization",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Indus_Valley_Civilisation|Ancient_Egypt|Mesopotamia|Ancient_Greece|Maya_civilization&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "historical_civilizations_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Historiographical consensus summaries",
            "Varying archeological chronologies"
        ]
    },
    {
        "domain_id": "02_general_knowledge",
        "domain_name": "General knowledge",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "02_03",
        "subtopic_name": "Discoveries and inventions",
        "candidate_title": "Major Scientific Discoveries and Technological Inventions Timeline Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Timeline_of_historic_inventions",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Printing_press|Steam_engine|Electricity|Transistor|Penicillin&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "discoveries_and_inventions_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Curated technological timeline narratives",
            "English focus"
        ]
    },
    {
        "domain_id": "02_general_knowledge",
        "domain_name": "General knowledge",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "02_04",
        "subtopic_name": "Everyday facts about the world",
        "candidate_title": "TriviaQA General World Knowledge Benchmark Samples",
        "source_platform": "Hugging Face",
        "publisher": "Hugging Face Contributor Community",
        "source_url": "https://huggingface.co/datasets/mandarjoshi/trivia_qa",
        "download_url": "https://datasets-server.huggingface.co/rows?dataset=mandarjoshi%2Ftrivia_qa&config=rc&split=train&offset=0&limit=100",
        "license": "Apache-2.0",
        "language": "en",
        "format": "json",
        "target_filename": "trivia_general_facts.json",
        "text_fields": [
            "question",
            "answer",
            "search_results"
        ],
        "limitations": [
            "Question-answer format",
            "Verification requires external checking"
        ]
    },
    {
        "domain_id": "03_mathematics",
        "domain_name": "Mathematics",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "03_01",
        "subtopic_name": "Arithmetic and percentages",
        "candidate_title": "GSM8K Grade School Arithmetic Word Problems",
        "source_platform": "Hugging Face",
        "publisher": "Hugging Face Contributor Community",
        "source_url": "https://huggingface.co/datasets/openai/gsm8k",
        "download_url": "https://raw.githubusercontent.com/openai/grade-school-math/master/grade_school_math/data/test.jsonl",
        "license": "MIT",
        "language": "en",
        "format": "jsonl",
        "target_filename": "gsm8k_arithmetic_word_problems.jsonl",
        "text_fields": [
            "question",
            "answer"
        ],
        "limitations": [
            "Grade-school multistep reasoning problems"
        ]
    },
    {
        "domain_id": "03_mathematics",
        "domain_name": "Mathematics",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "03_02",
        "subtopic_name": "Algebra and equations",
        "candidate_title": "Hendrycks MATH Algebra High-Level Mathematical Problems",
        "source_platform": "Hugging Face",
        "publisher": "Hugging Face Contributor Community",
        "source_url": "https://huggingface.co/datasets/themanas021/MATH-Algebra",
        "download_url": "https://datasets-server.huggingface.co/rows?dataset=themanas021%2FMATH-Algebra&config=default&split=train&offset=0&limit=100",
        "license": "MIT",
        "language": "en",
        "format": "json",
        "target_filename": "math_algebra_equations.json",
        "text_fields": [
            "problem",
            "solution"
        ],
        "limitations": [
            "LaTeX formatted mathematical equations",
            "Advanced competitive algebra"
        ]
    },
    {
        "domain_id": "03_mathematics",
        "domain_name": "Mathematics",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "03_03",
        "subtopic_name": "Geometry and measurements",
        "candidate_title": "MMLU High School Geometry Problem Explanations",
        "source_platform": "Hugging Face",
        "publisher": "Hugging Face Contributor Community",
        "source_url": "https://huggingface.co/datasets/cais/mmlu",
        "download_url": "https://datasets-server.huggingface.co/rows?dataset=cais%2Fmmlu&config=high_school_mathematics&split=test&offset=0&limit=100",
        "license": "MIT",
        "language": "en",
        "format": "json",
        "target_filename": "mmlu_high_school_geometry_math.json",
        "text_fields": [
            "question",
            "choices",
            "answer"
        ],
        "limitations": [
            "Multiple choice geometry problems",
            "Abstract spatial terminology"
        ]
    },
    {
        "domain_id": "03_mathematics",
        "domain_name": "Mathematics",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "03_04",
        "subtopic_name": "Statistics and probability",
        "candidate_title": "MMLU High School Statistics & Probability Problems",
        "source_platform": "Hugging Face",
        "publisher": "Hugging Face Contributor Community",
        "source_url": "https://huggingface.co/datasets/cais/mmlu",
        "download_url": "https://datasets-server.huggingface.co/rows?dataset=cais%2Fmmlu&config=high_school_statistics&split=test&offset=0&limit=100",
        "license": "MIT",
        "language": "en",
        "format": "json",
        "target_filename": "mmlu_statistics_probability.json",
        "text_fields": [
            "question",
            "choices",
            "answer"
        ],
        "limitations": [
            "Formal statistical questions",
            "Requires inferential interpretation"
        ]
    },
    {
        "domain_id": "04_physics_and_chemistry",
        "domain_name": "Physics and chemistry",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "04_01",
        "subtopic_name": "Motion, force, and energy",
        "candidate_title": "Conceptual Physics: Classical Mechanics, Motion, and Energy Corpus",
        "source_platform": "Hugging Face",
        "publisher": "Hugging Face Contributor Community",
        "source_url": "https://huggingface.co/datasets/cais/mmlu",
        "download_url": "https://datasets-server.huggingface.co/rows?dataset=cais%2Fmmlu&config=conceptual_physics&split=test&offset=0&limit=100",
        "license": "MIT",
        "language": "en",
        "format": "json",
        "target_filename": "conceptual_physics_mechanics.json",
        "text_fields": [
            "question",
            "choices",
            "answer"
        ],
        "limitations": [
            "Multiple-choice physics scenarios",
            "Focus on qualitative principles"
        ]
    },
    {
        "domain_id": "04_physics_and_chemistry",
        "domain_name": "Physics and chemistry",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "04_02",
        "subtopic_name": "Electricity and magnetism",
        "candidate_title": "College Physics: Electromagnetism and Circuits Knowledge Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Electromagnetism",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Electromagnetism|Magnetic_field|Electric_charge|Maxwell%27s_equations|Electromagnetic_induction&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "electricity_magnetism_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Technical physics prose",
            "Expository conceptual explanations"
        ]
    },
    {
        "domain_id": "04_physics_and_chemistry",
        "domain_name": "Physics and chemistry",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "04_03",
        "subtopic_name": "Chemical reactions",
        "candidate_title": "Chemical Reactions and Stoichiometric Thermodynamics Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Chemical_reaction",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Chemical_reaction|Stoichiometry|Combustion|Redox|Acid%E2%80%93base_reaction&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "chemical_reactions_stoichiometry_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Reaction kinetics and thermodynamic equilibria descriptions"
        ]
    },
    {
        "domain_id": "04_physics_and_chemistry",
        "domain_name": "Physics and chemistry",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "04_04",
        "subtopic_name": "Materials and their properties",
        "candidate_title": "Materials Science and Solid State Properties Knowledge Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Materials_science",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Materials_science|Strength_of_materials|Semiconductor|Superconductivity|Polymer&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "materials_science_properties.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Materials classification definitions and mechanical properties overview"
        ]
    },
    {
        "domain_id": "05_space_and_the_universe",
        "domain_name": "Space and the universe",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "05_01",
        "subtopic_name": "Planets and the solar system",
        "candidate_title": "Solar System Planets and Celestial Bodies Knowledge Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Solar_System",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Solar_System|Mars|Jupiter|Saturn|Exoplanet&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "solar_system_planets_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Planetary science overview",
            "Physical parameters included"
        ]
    },
    {
        "domain_id": "05_space_and_the_universe",
        "domain_name": "Space and the universe",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "05_02",
        "subtopic_name": "Stars and galaxies",
        "candidate_title": "Stellar Astrophysics and Galactic Evolution Knowledge Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Galaxy",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Galaxy|Milky_Way|Star|Supernova|Nebula&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "stars_and_galaxies_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Astrophysical definitions and deep space structures"
        ]
    },
    {
        "domain_id": "05_space_and_the_universe",
        "domain_name": "Space and the universe",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "05_03",
        "subtopic_name": "Black holes and cosmic phenomena",
        "candidate_title": "Black Holes and Relativistic Cosmic Phenomena Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Black_hole",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Black_hole|Gravitational_wave|Neutron_star|Gamma-ray_burst|Quasar&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "black_holes_cosmic_phenomena.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Theoretical physics and observational astrophysics summaries"
        ]
    },
    {
        "domain_id": "05_space_and_the_universe",
        "domain_name": "Space and the universe",
        "category": "Category A \u2014 Education, knowledge, and science",
        "subtopic_id": "05_04",
        "subtopic_name": "Space exploration and astronomy",
        "candidate_title": "MMLU College Astronomy Benchmark and Questions",
        "source_platform": "Hugging Face",
        "publisher": "Hugging Face Contributor Community",
        "source_url": "https://huggingface.co/datasets/cais/mmlu",
        "download_url": "https://datasets-server.huggingface.co/rows?dataset=cais%2Fmmlu&config=astronomy&split=test&offset=0&limit=100",
        "license": "MIT",
        "language": "en",
        "format": "json",
        "target_filename": "mmlu_astronomy_space_exploration.json",
        "text_fields": [
            "question",
            "choices",
            "answer"
        ],
        "limitations": [
            "Astronomy and space science evaluation"
        ]
    },
    {
        "domain_id": "06_nature_and_ecosystems",
        "domain_name": "Nature and ecosystems",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "06_01",
        "subtopic_name": "Forests and natural habitats",
        "candidate_title": "Forest Ecosystems and Terrestrial Habitats Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Forest_ecology",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Forest_ecology|Rainforest|Boreal_forest|Temperate_deciduous_forest|Old-growth_forest&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "forest_ecosystems_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Ecological terminology and canopy layers descriptions"
        ]
    },
    {
        "domain_id": "06_nature_and_ecosystems",
        "domain_name": "Nature and ecosystems",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "06_02",
        "subtopic_name": "Mountains and valleys",
        "candidate_title": "Mountain Geomorphology and Alpine Valleys Knowledge Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Mountain",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Mountain|Valley|Alpine_climate|Glacial_landform|Plate_tectonics&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "mountains_and_valleys_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Geological formation mechanisms and high-altitude biomes"
        ]
    },
    {
        "domain_id": "06_nature_and_ecosystems",
        "domain_name": "Nature and ecosystems",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "06_03",
        "subtopic_name": "Rivers and lakes",
        "candidate_title": "Limnology, Freshwater Rivers and Lakes Knowledge Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/River",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=River|Lake|Limnology|Riparian_zone|Wetland&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "rivers_and_lakes_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Freshwater hydrology and riparian ecology"
        ]
    },
    {
        "domain_id": "06_nature_and_ecosystems",
        "domain_name": "Nature and ecosystems",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "06_04",
        "subtopic_name": "Deserts and grasslands",
        "candidate_title": "Arid Ecosystems: Deserts, Steppes, and Grasslands Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Desert",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Desert|Grassland|Savanna|Steppe|Desertification&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "deserts_and_grasslands_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Arid climate dynamics and xerophytic vegetation"
        ]
    },
    {
        "domain_id": "07_trees_and_plants",
        "domain_name": "Trees and plants",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "07_01",
        "subtopic_name": "Tree species and their uses",
        "candidate_title": "Dendrology: Global Tree Species and Economic Uses Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Tree",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Tree|Oak|Pine|Teak|Eucalyptus&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "tree_species_uses_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Botanical classification and timber/industrial applications"
        ]
    },
    {
        "domain_id": "07_trees_and_plants",
        "domain_name": "Trees and plants",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "07_02",
        "subtopic_name": "Plant growth and reproduction",
        "candidate_title": "Plant Physiology, Photosynthesis, and Reproduction Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Plant_physiology",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Plant_physiology|Photosynthesis|Pollination|Seed_dispersal|Germination&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "plant_growth_reproduction_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Biochemical plant processes and developmental biology"
        ]
    },
    {
        "domain_id": "07_trees_and_plants",
        "domain_name": "Trees and plants",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "07_03",
        "subtopic_name": "Gardening and plant care",
        "candidate_title": "Horticultural Care, Composting, and Urban Gardening Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Gardening",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Gardening|Horticulture|Pruning|Compost|Companion_planting&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "gardening_and_plant_care_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Practical horticultural practices and cultivation techniques"
        ]
    },
    {
        "domain_id": "07_trees_and_plants",
        "domain_name": "Trees and plants",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "07_04",
        "subtopic_name": "Medicinal and useful plants",
        "candidate_title": "Ethnobotanical Pharmacology and Medicinal Plants Knowledge Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Medicinal_plants",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Medicinal_plants|Herbal_medicine|Pharmacognosy|Aloe_vera|Ginkgo_biloba&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "medicinal_plants_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Traditional pharmacognosy and botanical active compounds"
        ]
    },
    {
        "domain_id": "08_animals_and_wildlife",
        "domain_name": "Animals and wildlife",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "08_01",
        "subtopic_name": "Mammals and behavior",
        "candidate_title": "Mammalian Ethology, Social Structure, and Behavior Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Mammal",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Mammal|Animal_behaviour|Primate|Carnivora|Cetacea&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "mammals_and_behavior_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Zoological classification and behavioral ethology"
        ]
    },
    {
        "domain_id": "08_animals_and_wildlife",
        "domain_name": "Animals and wildlife",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "08_02",
        "subtopic_name": "Birds and migration",
        "candidate_title": "Ornithology: Bird Species and Avian Migration Systems Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Bird_migration",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Bird_migration|Ornithology|Flyway|Avian_navigation|Songbird&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "birds_and_migration_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Navigation mechanisms and seasonal migratory routes"
        ]
    },
    {
        "domain_id": "08_animals_and_wildlife",
        "domain_name": "Animals and wildlife",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "08_03",
        "subtopic_name": "Marine animals",
        "candidate_title": "Marine Biology, Pelagic and Coral Reef Animals Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Marine_biology",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Marine_biology|Coral_reef|Whale|Shark|Cephalopod&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "marine_animals_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Oceanic fauna and deep sea biological adaptations"
        ]
    },
    {
        "domain_id": "08_animals_and_wildlife",
        "domain_name": "Animals and wildlife",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "08_04",
        "subtopic_name": "Wildlife habitats and conservation",
        "candidate_title": "Wildlife Conservation and Biodiversity Protection Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Conservation_biology",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Conservation_biology|Endangered_species|IUCN_Red_List|Habitat_fragmentation|Rewilding&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "wildlife_conservation_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Conservation status methodologies and ecological restoration"
        ]
    },
    {
        "domain_id": "09_agriculture_and_farming",
        "domain_name": "Agriculture and farming",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "09_01",
        "subtopic_name": "Crop cultivation",
        "candidate_title": "Agronomy: Cereal and Legume Crop Cultivation Manual Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Agronomy",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Agronomy|Crop_rotation|Tillage|Wheat|Rice&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "crop_cultivation_agronomy_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Agricultural field management and crop yield factors"
        ]
    },
    {
        "domain_id": "09_agriculture_and_farming",
        "domain_name": "Agriculture and farming",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "09_02",
        "subtopic_name": "Soil fertility and management",
        "candidate_title": "Soil Science: Pedology, Nutrient Cycling, and Fertility Management Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Soil_fertility",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Soil_fertility|Humus|Nitrogen_cycle|Fertilizer|Soil_organic_matter&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "soil_fertility_management_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Chemical macronutrients (NPK) and pedological properties"
        ]
    },
    {
        "domain_id": "09_agriculture_and_farming",
        "domain_name": "Agriculture and farming",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "09_03",
        "subtopic_name": "Irrigation and water management",
        "candidate_title": "Agricultural Irrigation Systems and Water Conservation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Irrigation",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Irrigation|Drip_irrigation|Water_efficiency|Canal|Groundwater_recharge&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "irrigation_water_management_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Hydrological distribution techniques in arid and temperate farming"
        ]
    },
    {
        "domain_id": "09_agriculture_and_farming",
        "domain_name": "Agriculture and farming",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "09_04",
        "subtopic_name": "Harvesting and crop storage",
        "candidate_title": "Post-Harvest Grain Storage and Silo Preservation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Post-harvest_losses",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Post-harvest_losses|Silo|Grain_drying|Food_storage|Refrigeration&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "harvesting_crop_storage_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Spoilage prevention mechanisms and modern bulk grain storage"
        ]
    },
    {
        "domain_id": "10_weather_and_climate",
        "domain_name": "Weather and climate",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "10_01",
        "subtopic_name": "Rainfall and seasonal patterns",
        "candidate_title": "Meteorology: Monsoon Systems and Global Precipitation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Rain",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Rain|Monsoon|Precipitation|Water_cycle|Season&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "rainfall_seasonal_patterns_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Synoptic meteorological dynamics and global moisture circulation"
        ]
    },
    {
        "domain_id": "10_weather_and_climate",
        "domain_name": "Weather and climate",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "10_02",
        "subtopic_name": "Temperature and humidity",
        "candidate_title": "Atmospheric Thermodynamics: Humidity and Temperature Norms Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Humidity",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Humidity|Relative_humidity|Dew_point|Atmospheric_temperature|Lapse_rate&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "temperature_humidity_thermodynamics.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Psychrometric parameters and thermal stratification"
        ]
    },
    {
        "domain_id": "10_weather_and_climate",
        "domain_name": "Weather and climate",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "10_03",
        "subtopic_name": "Storms and severe weather",
        "candidate_title": "Severe Weather: Tropical Cyclones, Tornadoes, and Thunderstorms Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Tropical_cyclone",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Tropical_cyclone|Tornado|Thunderstorm|Blizzard|Supercell&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "severe_weather_storms_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Mesoscale convective systems and extreme atmospheric events"
        ]
    },
    {
        "domain_id": "10_weather_and_climate",
        "domain_name": "Weather and climate",
        "category": "Category B \u2014 Nature, environment, and agriculture",
        "subtopic_id": "10_04",
        "subtopic_name": "Climate patterns and their effects",
        "candidate_title": "Climatology: Climate Change and Oscillations Knowledge Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Climate_change",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Climate_change|El_Ni%C3%B1o%E2%80%93Southern_Oscillation|Global_warming|Carbon_cycle|Sea_level_rise&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "climate_patterns_effects_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Macro-climatological indices and historical environmental changes"
        ]
    },
    {
        "domain_id": "11_household_management",
        "domain_name": "Household management",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "11_01",
        "subtopic_name": "Cleaning and organization",
        "candidate_title": "Domestic Sanitation, Cleaning, and Household Organizing Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Cleaning",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Cleaning|Sanitation|Housekeeping|Decluttering|Detergent&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "cleaning_and_organization_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Domestic hygiene principles and chemical surfactant actions"
        ]
    },
    {
        "domain_id": "11_household_management",
        "domain_name": "Household management",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "11_02",
        "subtopic_name": "Laundry and clothing care",
        "candidate_title": "Textile Care, Garment Laundering, and Fabric Preservation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Laundry",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Laundry|Fabric_care_label|Stain|Dry_cleaning|Ironing&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "laundry_clothing_care_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Garment care symbolics and fabric maintenance procedures"
        ]
    },
    {
        "domain_id": "11_household_management",
        "domain_name": "Household management",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "11_03",
        "subtopic_name": "Household maintenance",
        "candidate_title": "Residential Infrastructure, Plumbing, and Home Maintenance Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Home_repair",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Home_repair|Plumbing|Electrical_wiring|HVAC|Weatherization&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "household_maintenance_repair_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Preventive home upkeep and mechanical diagnostics"
        ]
    },
    {
        "domain_id": "11_household_management",
        "domain_name": "Household management",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "11_04",
        "subtopic_name": "Daily household routines",
        "candidate_title": "Domestic Ergonomics and Daily Home Routines Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Homemaking",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Homemaking|Domestic_technology|Chore|Time_management|Work%E2%80%93family_conflict&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "daily_household_routines_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Domestic time allocation and household chore workflows"
        ]
    },
    {
        "domain_id": "12_cooking_and_food",
        "domain_name": "Cooking and food",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "12_01",
        "subtopic_name": "Recipes and cooking methods",
        "candidate_title": "Culinary Techniques, Gastronomy, and Recipes Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Cooking",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Cooking|Baking|Roasting|Saut%C3%A9ing|Sous_vide&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "recipes_cooking_methods_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Thermal food preparation and classical culinary techniques"
        ]
    },
    {
        "domain_id": "12_cooking_and_food",
        "domain_name": "Cooking and food",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "12_02",
        "subtopic_name": "Ingredients and substitutions",
        "candidate_title": "Food Ingredients, Seasonings, and Culinary Substitutions Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Ingredient",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Ingredient|Spice|Herb|Sugar_substitute|Flour&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "ingredients_substitutions_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Flavor profiles, culinary baking substitutes, and spices"
        ]
    },
    {
        "domain_id": "12_cooking_and_food",
        "domain_name": "Cooking and food",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "12_03",
        "subtopic_name": "Food storage and preservation",
        "candidate_title": "Food Science: Shelf-Life, Canning, and Preservation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Food_preservation",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Food_preservation|Canning|Pickling|Pasteurization|Freeze_drying&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "food_storage_preservation_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Microbiological stabilization and food safety storage guidelines"
        ]
    },
    {
        "domain_id": "12_cooking_and_food",
        "domain_name": "Cooking and food",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "12_04",
        "subtopic_name": "Meal preparation and planning",
        "candidate_title": "Meal Planning, Menu Design, and Nutritional Preparation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Meal_preparation",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Meal_preparation|Dietary_guidelines|Menu|Batch_cooking|Nutrient_density&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "meal_prep_planning_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Menu logistics and dietary nutritional planning"
        ]
    },
    {
        "domain_id": "13_personal_finance",
        "domain_name": "Personal finance",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "13_01",
        "subtopic_name": "Monthly budgeting",
        "candidate_title": "Personal Finance: Household Budgeting Strategies Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Budget",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Budget|Personal_budget|Zero-based_budgeting|Cash_flow|Savings_rate&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "monthly_budgeting_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Personal financial allocations and budget balancing principles"
        ]
    },
    {
        "domain_id": "13_personal_finance",
        "domain_name": "Personal finance",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "13_02",
        "subtopic_name": "Saving money",
        "candidate_title": "Emergency Funds, Frugal Living, and Compound Savings Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Saving",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Saving|Compound_interest|Emergency_fund|Frugality|Financial_independence&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "saving_money_finance_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Savings accumulation frameworks and interest compounding"
        ]
    },
    {
        "domain_id": "13_personal_finance",
        "domain_name": "Personal finance",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "13_03",
        "subtopic_name": "Managing everyday expenses",
        "candidate_title": "Consumer Expense Management and Debt Mitigation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Expense",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Expense|Credit_card_debt|Debt_consolidation|Fixed_cost|Variable_cost&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "everyday_expenses_management_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Recurring liability analysis and consumer debt mitigation"
        ]
    },
    {
        "domain_id": "13_personal_finance",
        "domain_name": "Personal finance",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "13_04",
        "subtopic_name": "Comparing costs and value",
        "candidate_title": "Consumer Economics: Cost-Benefit Analysis and Unit Valuation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Cost%E2%80%93benefit_analysis",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Cost%E2%80%93benefit_analysis|Opportunity_cost|Value_for_money|Unit_price|Total_cost_of_ownership&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "cost_value_comparison_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Valuation metrics and comparative consumer purchasing"
        ]
    },
    {
        "domain_id": "14_shopping_and_consumer_products",
        "domain_name": "Shopping and consumer products",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "14_01",
        "subtopic_name": "Product features and specifications",
        "candidate_title": "Product Design Specifications and Consumer Engineering Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Product_specification",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Product_specification|Bill_of_materials|Product_lifecycle|Quality_control|ISO_9000&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "product_features_specifications_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Engineering parameters and industrial quality standards"
        ]
    },
    {
        "domain_id": "14_shopping_and_consumer_products",
        "domain_name": "Shopping and consumer products",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "14_02",
        "subtopic_name": "Price and quality comparisons",
        "candidate_title": "Consumer Reports: Price-Quality Heuristics and Benchmarks Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Benchmarking",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Benchmarking|Comparative_advertising|Consumer_protection|Price_dispersion|Signaling_(economics)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "price_quality_comparisons_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Economic signaling and consumer testing heuristics"
        ]
    },
    {
        "domain_id": "14_shopping_and_consumer_products",
        "domain_name": "Shopping and consumer products",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "14_03",
        "subtopic_name": "Customer reviews and feedback",
        "candidate_title": "Customer Feedback Sentiment and Product Evaluation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Customer_review",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Customer_review|Net_Promoter|Customer_satisfaction|Word_of_mouth|Sentiment_analysis&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "customer_reviews_feedback_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Consumer sentiment metrics and qualitative feedback loops"
        ]
    },
    {
        "domain_id": "14_shopping_and_consumer_products",
        "domain_name": "Shopping and consumer products",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "14_04",
        "subtopic_name": "Warranties and returns",
        "candidate_title": "Consumer Rights: Warranty Law, Guarantees, and Return Policies Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Warranty",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Warranty|Extended_warranty|Product_liability|Cooling-off_period|Consumer_rights&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "warranties_and_returns_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Statutory warranty regulations and return merchandise rights"
        ]
    },
    {
        "domain_id": "15_daily_routines_and_productivity",
        "domain_name": "Daily routines and productivity",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "15_01",
        "subtopic_name": "Morning and evening routines",
        "candidate_title": "Circadian Synchronization and Daily Habit Rituals Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Circadian_rhythm",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Circadian_rhythm|Sleep_hygiene|Chronotype|Morning_routine|Habit&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "morning_evening_routines_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Sleep hygiene science and biological synchronization"
        ]
    },
    {
        "domain_id": "15_daily_routines_and_productivity",
        "domain_name": "Daily routines and productivity",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "15_02",
        "subtopic_name": "Task prioritization",
        "candidate_title": "Productivity Systems: Prioritization and Deep Work Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Getting_Things_Done",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Getting_Things_Done|Eisenhower_method|Action_item|Deep_work|Task_management&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "task_prioritization_productivity_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Action-oriented productivity frameworks"
        ]
    },
    {
        "domain_id": "15_daily_routines_and_productivity",
        "domain_name": "Daily routines and productivity",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "15_03",
        "subtopic_name": "Habit formation",
        "candidate_title": "Behavioral Psychology: Habit Loops and Automaticity Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Habit",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Habit|Operant_conditioning|Reinforcement|Behavioural_change_theories|Self-control&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "habit_formation_psychology_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Psychological cue-routine-reward architecture"
        ]
    },
    {
        "domain_id": "15_daily_routines_and_productivity",
        "domain_name": "Daily routines and productivity",
        "category": "Category C \u2014 Household and everyday life",
        "subtopic_id": "15_04",
        "subtopic_name": "Managing distractions",
        "candidate_title": "Cognitive Focus, Attention Economics, and Distraction Management Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Distraction",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Distraction|Attention_management|Digital_detox|Continuous_partial_attention|Flow_(psychology)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "managing_distractions_focus_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Attentional allocation and stimulus control strategies"
        ]
    },
    {
        "domain_id": "16_general_health_education",
        "domain_name": "General health education",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "16_01",
        "subtopic_name": "Common illnesses and symptoms",
        "candidate_title": "Medical Symptomatology and Clinical Pathology Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Symptom",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Symptom|Influenza|Common_cold|Fever|Hypertension&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "common_illnesses_symptoms_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Clinical presentations and diagnostic symptom profiles"
        ]
    },
    {
        "domain_id": "16_general_health_education",
        "domain_name": "General health education",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "16_02",
        "subtopic_name": "Preventive health practices",
        "candidate_title": "Public Health: Preventive Medicine and Prophylaxis Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Preventive_healthcare",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Preventive_healthcare|Vaccination|Screening_(medicine)|Epidemiology|Health_promotion&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "preventive_health_practices_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Primary and secondary prevention protocols"
        ]
    },
    {
        "domain_id": "16_general_health_education",
        "domain_name": "General health education",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "16_03",
        "subtopic_name": "Hygiene and infection prevention",
        "candidate_title": "Infection Control, Antisepsis, and Hygiene Standards Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Hygiene",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Hygiene|Hand_washing|Antiseptic|Transmission_(medicine)|Sterilization_(microbiology)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "hygiene_infection_prevention_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Aseptic techniques and pathogen transmission barriers"
        ]
    },
    {
        "domain_id": "16_general_health_education",
        "domain_name": "General health education",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "16_04",
        "subtopic_name": "Basic medical terminology",
        "candidate_title": "Medical Etymology, Anatomical Planes, and Clinical Terminology Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Medical_terminology",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Medical_terminology|List_of_medical_roots,_suffixes_and_prefixes|Anatomical_terms_of_location|Pathology|Physiology&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "basic_medical_terminology_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Standardized Greco-Latin morphological roots"
        ]
    },
    {
        "domain_id": "17_mental_health_and_wellbeing",
        "domain_name": "Mental health and wellbeing",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "17_01",
        "subtopic_name": "Stress management",
        "candidate_title": "Physiological and Cognitive Stress Regulation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Stress_management",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Stress_management|Cortisol|Chronic_stress|General_adaptation_syndrome|Psychological_resilience&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "stress_management_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Endocrine stress response and behavioral interventions"
        ]
    },
    {
        "domain_id": "17_mental_health_and_wellbeing",
        "domain_name": "Mental health and wellbeing",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "17_02",
        "subtopic_name": "Emotional awareness",
        "candidate_title": "Affective Psychology, Emotion Theory, and Granularity Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Emotional_intelligence",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Emotional_intelligence|Emotion|Self-awareness|Mood_(psychology)|Affect_(psychology)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "emotional_awareness_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Theories of emotion and emotional appraisal"
        ]
    },
    {
        "domain_id": "17_mental_health_and_wellbeing",
        "domain_name": "Mental health and wellbeing",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "17_03",
        "subtopic_name": "Relaxation and mindfulness",
        "candidate_title": "Mindfulness-Based Stress Reduction and Autogenic Relaxation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Mindfulness",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Mindfulness|Meditation|Progressive_muscle_relaxation|Autogenic_training|Breathing_exercise&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "relaxation_mindfulness_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Contemplative neuroscience and autonomic down-regulation"
        ]
    },
    {
        "domain_id": "17_mental_health_and_wellbeing",
        "domain_name": "Mental health and wellbeing",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "17_04",
        "subtopic_name": "Healthy coping strategies",
        "candidate_title": "Cognitive Behavioral Therapy (CBT) and Coping Mechanisms Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Coping",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Coping|Cognitive_behavioral_therapy|Defence_mechanism|Cognitive_restructuring|Problem-solving&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "healthy_coping_strategies_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Adaptive cognitive restructuring and emotional regulation"
        ]
    },
    {
        "domain_id": "18_fitness_and_exercise",
        "domain_name": "Fitness and exercise",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "18_01",
        "subtopic_name": "Cardiovascular exercise",
        "candidate_title": "Cardiovascular Conditioning, VO2 Max, and Aerobic Physiology Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Aerobic_exercise",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Aerobic_exercise|High-intensity_interval_training|VO2_max|Endurance_training|Heart_rate&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "cardiovascular_exercise_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Cardiorespiratory endurance and mitochondrial adaptation"
        ]
    },
    {
        "domain_id": "18_fitness_and_exercise",
        "domain_name": "Fitness and exercise",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "18_02",
        "subtopic_name": "Strength and resistance training",
        "candidate_title": "Resistance Training Mechanics and Neuromuscular Adaptation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Strength_training",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Strength_training|Isometric_exercise|Motor_unit|Compound_exercise|Calisthenics&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "strength_resistance_training_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Neuromuscular recruitment and force production principles"
        ]
    },
    {
        "domain_id": "18_fitness_and_exercise",
        "domain_name": "Fitness and exercise",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "18_03",
        "subtopic_name": "Flexibility and mobility",
        "candidate_title": "Joint Mobility, Range of Motion, and Flexibility Conditioning Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Flexibility_(anatomy)",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Flexibility_(anatomy)|Stretching|Joint_stability|Range_of_motion|Proprioceptive_neuromuscular_facilitation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "flexibility_mobility_conditioning_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Myofascial elasticity and articular mobility mechanics"
        ]
    },
    {
        "domain_id": "18_fitness_and_exercise",
        "domain_name": "Fitness and exercise",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "18_04",
        "subtopic_name": "Exercise routines and recovery",
        "candidate_title": "Exercise Periodization, Active Recovery, and DOMS Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Delayed_onset_muscle_soreness",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Delayed_onset_muscle_soreness|Sports_periodization|Active_recovery|Overtraining|Supercompensation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "exercise_routines_recovery_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Post-exercise physiological recovery and programming"
        ]
    },
    {
        "domain_id": "19_gym_and_bodybuilding",
        "domain_name": "Gym and bodybuilding",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "19_01",
        "subtopic_name": "Training splits and workout planning",
        "candidate_title": "Bodybuilding Workout Splits (PPL, Upper-Lower) Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Split_routine",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Split_routine|Weight_training|Circuit_training|Volume_(weight_training)|One-repetition_maximum&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "gym_workout_splits_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Hypertrophy training volume and muscle frequency"
        ]
    },
    {
        "domain_id": "19_gym_and_bodybuilding",
        "domain_name": "Gym and bodybuilding",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "19_02",
        "subtopic_name": "Muscle groups and exercise selection",
        "candidate_title": "Skeletal Muscular Anatomy and Biomechanical Exercise Selection Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Muscle_hypertrophy",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Muscle_hypertrophy|Quadriceps|Pectoralis_major|Latissimus_dorsi_muscle|Biceps&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "muscle_groups_exercise_selection_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Anatomical origins, insertions, and resistance curves"
        ]
    },
    {
        "domain_id": "19_gym_and_bodybuilding",
        "domain_name": "Gym and bodybuilding",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "19_03",
        "subtopic_name": "Progressive overload",
        "candidate_title": "Mechanisms of Progressive Overload and Mechanical Tension Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Progressive_overload",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Progressive_overload|Hypertrophy|Muscle_fatigue|Sarcoplasmic_hypertrophy|Workload&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "progressive_overload_mechanisms_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Hypertrophy stimulus variables and load progression"
        ]
    },
    {
        "domain_id": "19_gym_and_bodybuilding",
        "domain_name": "Gym and bodybuilding",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "19_04",
        "subtopic_name": "Rest, recovery, and training consistency",
        "candidate_title": "Athletic Sleep Architecture, Deloading, and Systemic Recovery Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Sleep_and_athletic_performance",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Sleep_and_athletic_performance|Growth_hormone|Overtraining_syndrome|Rest_period|Fatigue_(physiology)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "training_recovery_consistency_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Systemic recovery markers and athletic adherence"
        ]
    },
    {
        "domain_id": "20_nutrition_and_diet",
        "domain_name": "Nutrition and diet",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "20_01",
        "subtopic_name": "Macronutrients and micronutrients",
        "candidate_title": "Human Nutritional Biochemistry: Macronutrients and Micronutrients Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Nutrient",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Nutrient|Protein_(nutrient)|Carbohydrate|Dietary_fat|Vitamin&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "macronutrients_micronutrients_biochemistry.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Metabolic bioenergetics and vitamin/mineral biological roles"
        ]
    },
    {
        "domain_id": "20_nutrition_and_diet",
        "domain_name": "Nutrition and diet",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "20_02",
        "subtopic_name": "Balanced meal planning",
        "candidate_title": "Evidence-Based Dietetics and Nutritional Balance Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Healthy_diet",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Healthy_diet|Mediterranean_diet|Glycemic_index|Caloric_restriction|Dietary_fiber&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "balanced_diet_meal_planning_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Dietary patterns and chronic disease risk reduction"
        ]
    },
    {
        "domain_id": "20_nutrition_and_diet",
        "domain_name": "Nutrition and diet",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "20_03",
        "subtopic_name": "Hydration",
        "candidate_title": "Osmoregulation, Fluid Balance, and Electrolyte Hydration Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Water_intoxication",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Fluid_balance|Dehydration|Electrolyte|Hyponatremia|Osmoregulation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "hydration_electrolyte_balance_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Renal fluid handling and exercise hydration demands"
        ]
    },
    {
        "domain_id": "20_nutrition_and_diet",
        "domain_name": "Nutrition and diet",
        "category": "Category D \u2014 Health, fitness, and personal development",
        "subtopic_id": "20_04",
        "subtopic_name": "Food labels and nutritional values",
        "candidate_title": "Food Labeling Regulations and Nutritional Profiling Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Nutrition_facts_label",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Nutrition_facts_label|Daily_Value|Serving_size|Food_energy|Ingredients_list&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "food_labels_nutritional_values_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Regulatory nutritional standards and disclosure frameworks"
        ]
    },
    {
        "domain_id": "21_movies_and_cinema",
        "domain_name": "Movies and cinema",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "21_01",
        "subtopic_name": "Film genres and storytelling",
        "candidate_title": "Cinema Studies: Narrative Structure, Film Genres, and Tropes Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Film_genre",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Film_genre|Film_noir|Science_fiction_film|Screenwriting|Three-act_structure&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "film_genres_storytelling_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Cinematographic narrative conventions and taxonomy"
        ]
    },
    {
        "domain_id": "21_movies_and_cinema",
        "domain_name": "Movies and cinema",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "21_02",
        "subtopic_name": "Movie reviews and ratings",
        "candidate_title": "Film Criticism, Review Aggregation, and Rotten Tomatoes Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Film_criticism",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Film_criticism|Rotten_Tomatoes|Metacritic|Review_aggregator|Audience_reception&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "movie_reviews_ratings_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Aesthetic evaluation methodologies and consensus scoring"
        ]
    },
    {
        "domain_id": "21_movies_and_cinema",
        "domain_name": "Movies and cinema",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "21_03",
        "subtopic_name": "Filmmaking and production",
        "candidate_title": "Cinematography, Mise-en-sc\u00e8ne, and Film Production Technology Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Filmmaking",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Filmmaking|Cinematography|Mise-en-sc%C3%A8ne|Film_editing|Sound_design&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "filmmaking_production_technology_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Technical cinematography and audio-visual post-production"
        ]
    },
    {
        "domain_id": "21_movies_and_cinema",
        "domain_name": "Movies and cinema",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "21_04",
        "subtopic_name": "Box-office performance and audience reception",
        "candidate_title": "Film Industry Economics and Box Office Distribution Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Box_office",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Box_office|Film_budget|Theatrical_window|Blockbuster_(entertainment)|Box_Office_Mojo&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "box_office_audience_reception_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Theatrical financial performance and commercial dynamics"
        ]
    },
    {
        "domain_id": "22_television_series",
        "domain_name": "Television series",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "22_01",
        "subtopic_name": "Episode summaries",
        "candidate_title": "Television Studies: Episodic Structure and Series Synopses Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Television_show",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Television_show|Episode|Pilot_(television)|Cliffhanger|Season_finale&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "tv_episode_summaries_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Broadcast episodic frameworks and serial synopses"
        ]
    },
    {
        "domain_id": "22_television_series",
        "domain_name": "Television series",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "22_02",
        "subtopic_name": "Character development",
        "candidate_title": "Television Dramatic Character Arcs and Archetypes Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Character_arc",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Character_arc|Antihero|Protagonist|Ensemble_cast|Foil_(literature)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "tv_character_development_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Narrative psychological development across multi-episode runs"
        ]
    },
    {
        "domain_id": "22_television_series",
        "domain_name": "Television series",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "22_03",
        "subtopic_name": "Season comparisons",
        "candidate_title": "Television Serial Continuity, Showrunning, and Season Comparisons Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Showrunner",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Showrunner|Golden_Age_of_Television_(2000s%E2%80%93present)|Serial_(radio_and_television)|Syndication|Television_pilot&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "tv_season_comparisons_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Comparative structural changes across multi-year runs"
        ]
    },
    {
        "domain_id": "22_television_series",
        "domain_name": "Television series",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "22_04",
        "subtopic_name": "Story structure and plot progression",
        "candidate_title": "Television Dramaturgy: Serialized vs Procedural Story Architecture Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Narrative_structure",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Narrative_structure|Procedural_drama|Story_arc|Foreshadowing|Plot_device&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "story_structure_plot_progression_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Episodic progression models and dramaturgical pacing"
        ]
    },
    {
        "domain_id": "23_pakistani_dramas",
        "domain_name": "Pakistani dramas",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "23_01",
        "subtopic_name": "Drama summaries and themes",
        "candidate_title": "Pakistani Television Drama Industry and Thematic Summaries Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Pakistani_dramas",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Pakistani_dramas|Humsafar|Zindagi_Gulzar_Hai|Parizaad|Dhoop_Kinare&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "pakistani_drama_summaries_themes.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Thematic overviews of prominent Urdu serials and cultural impact"
        ]
    },
    {
        "domain_id": "23_pakistani_dramas",
        "domain_name": "Pakistani dramas",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "23_02",
        "subtopic_name": "Character relationships",
        "candidate_title": "Interpersonal Relationships and Family Dynamics in Pakistani Serials Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Hum_TV",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Hum_TV|ARY_Digital|Geo_Entertainment|Dastaan_(TV_series)|Alpha_Bravo_Charlie&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "pakistani_drama_character_relationships.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Relational conflicts and social dramatization profiles"
        ]
    },
    {
        "domain_id": "23_pakistani_dramas",
        "domain_name": "Pakistani dramas",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "23_03",
        "subtopic_name": "Acting and direction reviews",
        "candidate_title": "Pakistani Television Directorial Styles and Critical Accolades Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Lux_Style_Awards",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Lux_Style_Awards|Hum_Awards|Sultana_Siddiqui|Nadeem_Baig_(director)|Umera_Ahmad&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "pakistani_drama_acting_direction_reviews.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Critical reception of scripts, direction, and awards"
        ]
    },
    {
        "domain_id": "23_pakistani_dramas",
        "domain_name": "Pakistani dramas",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "23_04",
        "subtopic_name": "Audience ratings and reception",
        "candidate_title": "Broadcast Viewership, TRPs, and Digital Reach of Pakistani Dramas Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Television_in_Pakistan",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Television_in_Pakistan|Target_rating_point|Pakistan_Electronic_Media_Regulatory_Authority|Urdu_1|A-Plus_TV&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "pakistani_drama_audience_ratings.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Rating methodologies and digital diaspora viewership trends"
        ]
    },
    {
        "domain_id": "24_online_streaming_platforms",
        "domain_name": "Online streaming platforms",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "24_01",
        "subtopic_name": "Subscription plans and features",
        "candidate_title": "Streaming Video On Demand (SVOD) Tiers and Platform Architecture Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Streaming_media",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Streaming_media|Subscription_business_model|Over-the-top_media_service|Video_on_demand|Digital_rights_management&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "streaming_subscription_plans_features.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Commercial monetization structures and digital distribution tiers"
        ]
    },
    {
        "domain_id": "24_online_streaming_platforms",
        "domain_name": "Online streaming platforms",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "24_02",
        "subtopic_name": "Content discovery and recommendations",
        "candidate_title": "Recommender Systems and Algorithmic Discovery in Streaming Platforms Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Recommender_system",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Recommender_system|Collaborative_filtering|Content-based_filtering|Cold_start_(computing)|Netflix_Prize&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "streaming_content_discovery_recommendations.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Algorithmic curation and user personalization mechanics"
        ]
    },
    {
        "domain_id": "24_online_streaming_platforms",
        "domain_name": "Online streaming platforms",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "24_03",
        "subtopic_name": "Viewing habits",
        "candidate_title": "Consumer Binge-Watching and Digital Media Consumption Patterns Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Binge-watching",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Binge-watching|Audience_measurement|Customer_attrition|Cord-cutting|Attention_span&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "streaming_viewing_habits_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Behavioral consumption metrics and media psychological effects"
        ]
    },
    {
        "domain_id": "24_online_streaming_platforms",
        "domain_name": "Online streaming platforms",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "24_04",
        "subtopic_name": "Platform usability and customer feedback",
        "candidate_title": "Streaming Interface Usability, Buffering Latency, and UX Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Quality_of_experience",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Quality_of_experience|Adaptive_bitrate_streaming|Buffering_(telecommunication)|Usability|User_experience&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "streaming_platform_usability_feedback.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Network buffering diagnostics and consumer UX criteria"
        ]
    },
    {
        "domain_id": "25_books_and_literature",
        "domain_name": "Books and literature",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "25_01",
        "subtopic_name": "Fiction genres",
        "candidate_title": "Literary Theory: Major Literary and Fiction Genres Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Literary_genre",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Literary_genre|Historical_fiction|Science_fiction|Gothic_fiction|Magical_realism&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "literary_fiction_genres_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Taxonomic definitions of fictional styles and narrative conventions"
        ]
    },
    {
        "domain_id": "25_books_and_literature",
        "domain_name": "Books and literature",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "25_02",
        "subtopic_name": "Book summaries and reviews",
        "candidate_title": "Project Gutenberg Classic Literature Corpus Extracts",
        "source_platform": "Project Gutenberg",
        "publisher": "Project Gutenberg Contributor Community",
        "source_url": "https://www.gutenberg.org/",
        "download_url": "https://www.gutenberg.org/cache/epub/11/pg11.txt",
        "license": "Public Domain",
        "language": "en",
        "format": "txt",
        "target_filename": "alice_in_wonderland_gutenberg.txt",
        "text_fields": [
            "text"
        ],
        "limitations": [
            "Full unencumbered classic literary text"
        ]
    },
    {
        "domain_id": "25_books_and_literature",
        "domain_name": "Books and literature",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "25_03",
        "subtopic_name": "Authors and literary styles",
        "candidate_title": "Comparative Stylistics: Prose Voice and Authorial Techniques Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Style_(fiction)",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Style_(fiction)|Stream_of_consciousness|Point_of_view_(literature)|Tone_(literature)|Voice_(writing)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "authors_literary_styles_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Syntactic and stylistic narrative techniques"
        ]
    },
    {
        "domain_id": "25_books_and_literature",
        "domain_name": "Books and literature",
        "category": "Category E \u2014 Entertainment and media",
        "subtopic_id": "25_04",
        "subtopic_name": "Themes, symbolism, and character analysis",
        "candidate_title": "Literary Analysis: Motifs, Symbolism, and Archetypes Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Theme_(literature)",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Theme_(literature)|Motif_(narrative)|Symbolism_(arts)|Archetype|Protagonist&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "literary_themes_symbolism_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Hermeneutic analysis frameworks and symbolic interpretation"
        ]
    },
    {
        "domain_id": "26_cricket",
        "domain_name": "Cricket",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "26_01",
        "subtopic_name": "Rules and match formats",
        "candidate_title": "Laws of Cricket, Test, ODI, and T20 Format Regulations Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Laws_of_Cricket",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Laws_of_Cricket|Test_cricket|One_Day_International|Twenty20|Decision_Review_System&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "cricket_rules_formats_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "MCC official regulations and DRS adjudications"
        ]
    },
    {
        "domain_id": "26_cricket",
        "domain_name": "Cricket",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "26_02",
        "subtopic_name": "Player statistics",
        "candidate_title": "Cricket Analytics: Batting Averages, Economy, and Strike Rates Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Cricket_statistics",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Cricket_statistics|Batting_average|Bowling_average|Economy_rate|Strike_rate&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "cricket_player_statistics_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Statistical metrics of player performance"
        ]
    },
    {
        "domain_id": "26_cricket",
        "domain_name": "Cricket",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "26_03",
        "subtopic_name": "Match summaries",
        "candidate_title": "Historic Cricket Match Summaries and Commentary Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/History_of_cricket",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=History_of_cricket|The_Ashes|Cricket_World_Cup|1992_Cricket_World_Cup|2019_Cricket_World_Cup&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "cricket_match_summaries_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Innings recaps and tournament milestones"
        ]
    },
    {
        "domain_id": "26_cricket",
        "domain_name": "Cricket",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "26_04",
        "subtopic_name": "Batting and bowling strategies",
        "candidate_title": "Tactical Cricket: Swing, Spin Variations, and Field Placements Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Bowling_(cricket)",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Bowling_(cricket)|Batting_(cricket)|Swing_bowling|Spin_bowling|Fielding_(cricket)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "cricket_batting_bowling_strategies.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Technical aerodynamics of swing and tactical captaincy setups"
        ]
    },
    {
        "domain_id": "27_football",
        "domain_name": "Football",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "27_01",
        "subtopic_name": "Rules and competitions",
        "candidate_title": "IFAB Laws of the Game and International Football Competitions Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Laws_of_the_Game_(association_football)",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Laws_of_the_Game_(association_football)|FIFA_World_Cup|UEFA_Champions_League|Offside_(association_football)|Video_assistant_referee&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "football_rules_competitions_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Official IFAB codified rules and tournament structures"
        ]
    },
    {
        "domain_id": "27_football",
        "domain_name": "Football",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "27_02",
        "subtopic_name": "Player and team statistics",
        "candidate_title": "Association Football Analytics: Expected Goals (xG) and Metrics Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Association_football_tactics_and_skills",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Association_football_tactics_and_skills|Clean_sheet|Assist_(association_football)|Cap_(sport)|Premier_League&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "football_player_team_statistics.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Performance indices and tracking data"
        ]
    },
    {
        "domain_id": "27_football",
        "domain_name": "Football",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "27_03",
        "subtopic_name": "Match reports",
        "candidate_title": "Classic International Football Match Reports and Chronicles Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Miracle_of_Bern",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Miracle_of_Bern|2014_FIFA_World_Cup_semi-final|1966_FIFA_World_Cup_final|2022_FIFA_World_Cup_final|Maracanazo&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "football_match_reports_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Detailed journalistic chronicles of historic finals"
        ]
    },
    {
        "domain_id": "27_football",
        "domain_name": "Football",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "27_04",
        "subtopic_name": "Formations and tactics",
        "candidate_title": "Tactical Football Theory: Gegenpressing, Tiki-Taka, and 4-3-3 Systems Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Formation_(association_football)",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Formation_(association_football)|Total_Football|Tiki-taka|Counter-attack|Zonal_marking&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "football_formations_tactics_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Spatial pitch control, defensive pressing, and transition play"
        ]
    },
    {
        "domain_id": "28_other_sports",
        "domain_name": "Other sports",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "28_01",
        "subtopic_name": "Badminton and tennis",
        "candidate_title": "Racquet Sports: Tennis and Badminton Technical Play Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Tennis",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Tennis|Badminton|Grand_Slam_(tennis)|Serve_(tennis)|Smash_(tennis)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "badminton_tennis_racquet_sports.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Court geometry, stroke biomechanics, and rules"
        ]
    },
    {
        "domain_id": "28_other_sports",
        "domain_name": "Other sports",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "28_02",
        "subtopic_name": "Hockey and basketball",
        "candidate_title": "Invasion Sports: Basketball Offense and Ice/Field Hockey Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Basketball",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Basketball|Ice_hockey|Field_hockey|Pick_and_roll|Fast_break&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "hockey_basketball_sports_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Tactical set pieces and transition offensive execution"
        ]
    },
    {
        "domain_id": "28_other_sports",
        "domain_name": "Other sports",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "28_03",
        "subtopic_name": "Athletics and running",
        "candidate_title": "Track and Field: Sprinting Biomechanics, Distance Running, and Decathlon Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Sport_of_athletics",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Sport_of_athletics|Sprint_(running)|Marathon|Decathlon|Long_jump&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "athletics_and_running_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Locomotor biomechanics and physiological pacing"
        ]
    },
    {
        "domain_id": "28_other_sports",
        "domain_name": "Other sports",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "28_04",
        "subtopic_name": "Swimming and martial arts",
        "candidate_title": "Aquatics and Combat Disciplines: Swimming Strokes and Martial Arts Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Swimming_(sport)",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Swimming_(sport)|Freestyle_swimming|Martial_arts|Judo|Taekwondo&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "swimming_martial_arts_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Hydrodynamic propulsion and martial combat principles"
        ]
    },
    {
        "domain_id": "29_gaming_and_esports",
        "domain_name": "Gaming and esports",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "29_01",
        "subtopic_name": "Game genres and mechanics",
        "candidate_title": "Ludology: Game Design Mechanics, Core Loops, and Genres Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Game_mechanics",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Game_mechanics|Video_game_genre|Role-playing_video_game|First-person_shooter|Roguelike&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "game_genres_mechanics_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Game loop architecture and emergent interactive design"
        ]
    },
    {
        "domain_id": "29_gaming_and_esports",
        "domain_name": "Gaming and esports",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "29_02",
        "subtopic_name": "Player strategies and tactics",
        "candidate_title": "Competitive Video Gaming: Meta-Strategies, Positioning, and Builds Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Multiplayer_online_battle_arena",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Multiplayer_online_battle_arena|Real-time_strategy|Speedrunning|Micro_(video_games)|Gamer&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "gaming_strategies_tactics_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Tactical resource allocation and cooperative execution"
        ]
    },
    {
        "domain_id": "29_gaming_and_esports",
        "domain_name": "Gaming and esports",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "29_03",
        "subtopic_name": "Game reviews",
        "candidate_title": "Video Game Journalism, Ludic Evaluation, and Critical Reviews Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Video_game_journalism",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Video_game_journalism|The_Game_Awards|Game_criticism|Gameplay|Review_bombing&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "video_game_reviews_journalism_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Evaluation of interactive ludonarrative harmony"
        ]
    },
    {
        "domain_id": "29_gaming_and_esports",
        "domain_name": "Gaming and esports",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "29_04",
        "subtopic_name": "Esports performance and statistics",
        "candidate_title": "Professional Esports Tournaments, Prize Pools, and Player Metrics Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Esports",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Esports|The_International_(Dota_2)|League_of_Legends_World_Championship|Major_Championship_(Counter-Strike)|Evolution_Championship_Series&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "esports_performance_statistics_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Championship records and competitive tournament formats"
        ]
    },
    {
        "domain_id": "30_hobbies_and_creative_activities",
        "domain_name": "Hobbies and creative activities",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "30_01",
        "subtopic_name": "Drawing and painting",
        "candidate_title": "Visual Arts Theory: Painting Techniques, Media, and Chiaroscuro Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Painting",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Painting|Drawing|Color_theory|Chiaroscuro|Oil_painting&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "drawing_and_painting_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Color harmonies and pigment composition mechanics"
        ]
    },
    {
        "domain_id": "30_hobbies_and_creative_activities",
        "domain_name": "Hobbies and creative activities",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "30_02",
        "subtopic_name": "Photography as a hobby, using text only",
        "candidate_title": "Text-Based Photographic Theory: Exposure Triangle, Composition, and Optics Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Photography",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Photography|Aperture|Shutter_speed|Film_speed|Rule_of_thirds&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "photography_theory_text_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Strict text-based exposure mechanics and framing"
        ]
    },
    {
        "domain_id": "30_hobbies_and_creative_activities",
        "domain_name": "Hobbies and creative activities",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "30_03",
        "subtopic_name": "Gardening and DIY crafts",
        "candidate_title": "DIY Crafting, Joinery, and Domestic Handicrafts Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Do_it_yourself",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Do_it_yourself|Woodworking|Handicraft|Pottery|Upcycling&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "diy_crafts_woodworking_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Manual fabrication techniques and tool handling"
        ]
    },
    {
        "domain_id": "30_hobbies_and_creative_activities",
        "domain_name": "Hobbies and creative activities",
        "category": "Category F \u2014 Sports, hobbies, and recreation",
        "subtopic_id": "30_04",
        "subtopic_name": "Music theory and instrument learning, using text only",
        "candidate_title": "Text-Based Musicology: Scales, Harmony, and Instrument Architecture Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Music_theory",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Music_theory|Scale_(music)|Chord_(music)|Circle_of_fifths|Musical_notation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "music_theory_text_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Strict text-based harmonic structures and intervals"
        ]
    },
    {
        "domain_id": "31_economics",
        "domain_name": "Economics",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "31_01",
        "subtopic_name": "Inflation and purchasing power",
        "candidate_title": "Macroeconomics: Inflation, Consumer Price Index, and Purchasing Power Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Inflation",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Inflation|Consumer_price_index|Purchasing_power|Hyperinflation|Central_bank&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "inflation_purchasing_power_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Monetary policy economics and price index formulation"
        ]
    },
    {
        "domain_id": "31_economics",
        "domain_name": "Economics",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "31_02",
        "subtopic_name": "Supply and demand",
        "candidate_title": "Microeconomic Equilibrium: Price Elasticity and Market Forces Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Supply_and_demand",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Supply_and_demand|Price_elasticity_of_demand|Economic_equilibrium|Deadweight_loss|Consumer_surplus&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "supply_and_demand_microeconomics.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Market clearing dynamics and elasticity coefficients"
        ]
    },
    {
        "domain_id": "31_economics",
        "domain_name": "Economics",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "31_03",
        "subtopic_name": "Employment and wages",
        "candidate_title": "Labor Economics: Unemployment, Wage Determination, and Human Capital Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Labour_economics",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Labour_economics|Unemployment|Minimum_wage|Human_capital|Collective_bargaining&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "employment_wages_labor_economics.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Labor market equilibrium and wage rigidity"
        ]
    },
    {
        "domain_id": "31_economics",
        "domain_name": "Economics",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "31_04",
        "subtopic_name": "Production and economic growth",
        "candidate_title": "Macroeconomic Growth Theory: GDP, Productivity, and Solow Models Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Economic_growth",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Economic_growth|Gross_domestic_product|Total_factor_productivity|Solow%E2%80%93Swan_model|Capital_accumulation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "production_economic_growth_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Production functions and technological capital deepening"
        ]
    },
    {
        "domain_id": "32_e_commerce",
        "domain_name": "E-commerce",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "32_01",
        "subtopic_name": "Online ordering and checkout",
        "candidate_title": "E-Commerce Architecture: Shopping Cart, Payment Gateways, and Checkout UX Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/E-commerce",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=E-commerce|Payment_gateway|Shopping_cart_software|Abandonment_rate|Online_shopping&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "online_ordering_checkout_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Checkout funnel friction and payment encryption standards"
        ]
    },
    {
        "domain_id": "32_e_commerce",
        "domain_name": "E-commerce",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "32_02",
        "subtopic_name": "Product listings and descriptions",
        "candidate_title": "Pakistan Biggest E-Commerce Real World Catalog Dataset",
        "source_platform": "Hugging Face",
        "publisher": "Hugging Face Contributor Community",
        "source_url": "https://huggingface.co/datasets/sajeelkazmi/PakistanBiggestEcommerceDatasetCleaned",
        "download_url": "https://datasets-server.huggingface.co/rows?dataset=sajeelkazmi%2FPakistanBiggestEcommerceDatasetCleaned&config=default&split=train&offset=0&limit=100",
        "license": "Apache-2.0",
        "language": "en",
        "format": "json",
        "target_filename": "ecommerce_pakistan_catalog.json",
        "text_fields": [
            "item_id",
            "category_name_1",
            "status",
            "price"
        ],
        "limitations": [
            "Real-world South Asian e-commerce retail transactions"
        ]
    },
    {
        "domain_id": "32_e_commerce",
        "domain_name": "E-commerce",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "32_03",
        "subtopic_name": "Shipping and delivery",
        "candidate_title": "Logistics Engineering: Last-Mile Delivery, Fulfillment, and Tracking Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Last_mile_(transportation)",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Last_mile_(transportation)|Order_fulfillment|Supply_chain_management|Freight_forwarding|Package_tracking&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "shipping_and_delivery_logistics_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Distribution network routing and courier logistics"
        ]
    },
    {
        "domain_id": "32_e_commerce",
        "domain_name": "E-commerce",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "32_04",
        "subtopic_name": "Returns, refunds, and customer support",
        "candidate_title": "Reverse Logistics: RMA, Refund Policies, and Merchant Dispute Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Reverse_logistics",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Reverse_logistics|Return_merchandise_authorization|Customer_service|Chargeback|Help_desk&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "returns_refunds_support_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Merchant return workflows and dispute adjudication"
        ]
    },
    {
        "domain_id": "33_small_businesses_and_entrepreneurship",
        "domain_name": "Small businesses and entrepreneurship",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "33_01",
        "subtopic_name": "Business ideas and market research",
        "candidate_title": "Entrepreneurship: Value Proposition, TAM/SAM/SOM, and Market Feasibility Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Entrepreneurship",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Entrepreneurship|Market_research|Business_model|Business_plan|Feasibility_study&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "business_ideas_market_research_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Venture ideation and market sizing methodologies"
        ]
    },
    {
        "domain_id": "33_small_businesses_and_entrepreneurship",
        "domain_name": "Small businesses and entrepreneurship",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "33_02",
        "subtopic_name": "Startup costs and budgeting",
        "candidate_title": "Venture Finance: Seed Capital, Burn Rate, and Startup Budgeting Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Startup_company",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Startup_company|Seed_money|Venture_capital|Burn_rate|Working_capital&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "startup_costs_budgeting_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Financial runway management and initial capital expenditure"
        ]
    },
    {
        "domain_id": "33_small_businesses_and_entrepreneurship",
        "domain_name": "Small businesses and entrepreneurship",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "33_03",
        "subtopic_name": "Customer acquisition",
        "candidate_title": "SMB Growth: Customer Acquisition Cost (CAC), Funnels, and Lead Generation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Customer_acquisition",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Customer_acquisition|Lead_generation|Purchase_funnel|Customer_lifetime_value|Inbound_marketing&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "customer_acquisition_growth_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Acquisition metrics and conversion optimization"
        ]
    },
    {
        "domain_id": "33_small_businesses_and_entrepreneurship",
        "domain_name": "Small businesses and entrepreneurship",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "33_04",
        "subtopic_name": "Business operations and growth",
        "candidate_title": "Small Business Operations: Standard Operating Procedures and Scaling Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Business_operations",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Business_operations|Standard_operating_procedure|Small_business|Economies_of_scale|Franchising&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "business_operations_growth_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Operational efficiency and scaling milestones"
        ]
    },
    {
        "domain_id": "34_marketing_and_advertising",
        "domain_name": "Marketing and advertising",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "34_01",
        "subtopic_name": "Brand positioning",
        "candidate_title": "Strategic Marketing: Brand Equity, Positioning, and Archetypes Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Brand",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Brand|Positioning_(marketing)|Brand_equity|Unique_selling_proposition|Corporate_identity&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "brand_positioning_marketing_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Perceptual mapping and competitive differentiation"
        ]
    },
    {
        "domain_id": "34_marketing_and_advertising",
        "domain_name": "Marketing and advertising",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "34_02",
        "subtopic_name": "Advertising strategies",
        "candidate_title": "Advertising Theory: Copywriting, AIDA Model, and Media Planning Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Advertising",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Advertising|Copywriting|AIDA_(marketing)|Media_planning|Advertising_campaign&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "advertising_strategies_theory_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Persuasion models and multi-channel media buys"
        ]
    },
    {
        "domain_id": "34_marketing_and_advertising",
        "domain_name": "Marketing and advertising",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "34_03",
        "subtopic_name": "Customer segmentation",
        "candidate_title": "Market Segmentation: Demographics, Psychographics, and Behavioral Clusters Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Market_segmentation",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Market_segmentation|Target_audience|Persona_(user_experience)|Psychographics|Demographic_profile&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "customer_segmentation_clusters_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Targeted persona construction and demographic stratification"
        ]
    },
    {
        "domain_id": "34_marketing_and_advertising",
        "domain_name": "Marketing and advertising",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "34_04",
        "subtopic_name": "Campaign performance and engagement",
        "candidate_title": "Marketing Analytics: CTR, ROAS, and Attribution Modeling Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Marketing_performance_measurement_and_management",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Marketing_performance_measurement_and_management|Click-through_rate|Conversion_rate|Attribution_(marketing)|Key_performance_indicator&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "campaign_performance_engagement_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Digital engagement attribution and conversion analytics"
        ]
    },
    {
        "domain_id": "35_jobs_and_careers",
        "domain_name": "Jobs and careers",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "35_01",
        "subtopic_name": "Job descriptions and requirements",
        "candidate_title": "Occupational Competencies and Standard Job Descriptions Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Job_description",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Job_description|Profession|Occupation|Job_analysis|Recruitment&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "job_descriptions_requirements_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Competency prerequisites and role classification"
        ]
    },
    {
        "domain_id": "35_jobs_and_careers",
        "domain_name": "Jobs and careers",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "35_02",
        "subtopic_name": "Resume and interview preparation",
        "candidate_title": "Career Development: Resume Crafting and Behavioral Interviewing Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/R%C3%A9sum%C3%A9",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=R%C3%A9sum%C3%A9|Job_interview|Curriculum_vitae|Cover_letter|Situation,_task,_action_and_result&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "resume_interview_prep_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "STAR interview methodology and resume structuring"
        ]
    },
    {
        "domain_id": "35_jobs_and_careers",
        "domain_name": "Jobs and careers",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "35_03",
        "subtopic_name": "Career planning",
        "candidate_title": "Organizational Psychology: Career Paths, Mentorship, and Trajectories Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Career_development",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Career_development|Mentorship|Promotion_(rank)|Skill_management|Continuing_education&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "career_planning_development_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Career ladder progression and skill gap bridging"
        ]
    },
    {
        "domain_id": "35_jobs_and_careers",
        "domain_name": "Jobs and careers",
        "category": "Category G \u2014 Business, economy, and commerce",
        "subtopic_id": "35_04",
        "subtopic_name": "Workplace skills and professional development",
        "candidate_title": "Workplace Soft Skills, Leadership, and Professional Development Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Soft_skills",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Soft_skills|Communication|Leadership|Teamwork|Workplace_conflict&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "workplace_skills_professional_development.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Executive presence, active listening, and conflict de-escalation"
        ]
    },
    {
        "domain_id": "36_websites_and_web_services",
        "domain_name": "Websites and web services",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "36_01",
        "subtopic_name": "Website usability",
        "candidate_title": "HCI Usability Engineering: Nielsen Norman Heuristics and User Flow Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Usability",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Usability|Heuristic_evaluation|User_interface_design|Usability_testing|Human%E2%80%93computer_interaction&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "website_usability_heuristics_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Nielsen's 10 heuristics and cognitive walkthroughs"
        ]
    },
    {
        "domain_id": "36_websites_and_web_services",
        "domain_name": "Websites and web services",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "36_02",
        "subtopic_name": "Navigation and information structure",
        "candidate_title": "Information Architecture: Taxonomies, Sitemaps, and Navigation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Information_architecture",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Information_architecture|Site_map|Breadcrumb_navigation|Faceted_search|Taxonomy_(general)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "information_architecture_navigation_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Ontological hierarchies and faceted navigation principles"
        ]
    },
    {
        "domain_id": "36_websites_and_web_services",
        "domain_name": "Websites and web services",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "36_03",
        "subtopic_name": "Accessibility and readability",
        "candidate_title": "Web Accessibility: W3C WCAG Guidelines and Readability Standards Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Web_accessibility",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Web_accessibility|Web_Content_Accessibility_Guidelines|Screen_reader|Readability|Color_blindness&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "web_accessibility_wcag_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "WCAG 2.1 compliance criteria and assistive tech support"
        ]
    },
    {
        "domain_id": "36_websites_and_web_services",
        "domain_name": "Websites and web services",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "36_04",
        "subtopic_name": "Website performance descriptions and user feedback",
        "candidate_title": "Web Performance Engineering: Core Web Vitals and Latency Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Web_performance",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Web_performance|PageSpeed_Insights|Content_delivery_network|Minification_(programming)|Browser_cache&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "website_performance_vitals_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "LCP, FID, CLS performance thresholds and caching"
        ]
    },
    {
        "domain_id": "37_computers_and_operating_systems",
        "domain_name": "Computers and operating systems",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "37_01",
        "subtopic_name": "Hardware specifications",
        "candidate_title": "Computer Architecture: Microprocessors, Memory Busses, and Storage Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Computer_hardware",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Computer_hardware|Central_processing_unit|Random-access_memory|Solid-state_drive|PCI_Express&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "computer_hardware_specifications_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Microarchitecture bus widths, cache hierarchies, and protocols"
        ]
    },
    {
        "domain_id": "37_computers_and_operating_systems",
        "domain_name": "Computers and operating systems",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "37_02",
        "subtopic_name": "Operating system features",
        "candidate_title": "Operating Systems Theory: Kernels, Virtual Memory, and Scheduling Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Operating_system",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Operating_system|Kernel_(operating_system)|Virtual_memory|Scheduling_(computing)|File_system&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "operating_system_features_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Process scheduling algorithms and page fault handling"
        ]
    },
    {
        "domain_id": "37_computers_and_operating_systems",
        "domain_name": "Computers and operating systems",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "37_03",
        "subtopic_name": "Computer troubleshooting",
        "candidate_title": "IT Systems Administration: Hardware Diagnostics and Error Remediation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Troubleshooting",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Troubleshooting|Blue_screen_of_death|Device_driver|Power-on_self-test|Firmware&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "computer_troubleshooting_diagnostics_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "POST codes, memory fault isolation, and driver recovery"
        ]
    },
    {
        "domain_id": "37_computers_and_operating_systems",
        "domain_name": "Computers and operating systems",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "37_04",
        "subtopic_name": "Device maintenance and upgrades",
        "candidate_title": "PC Maintenance: Thermal Management, BIOS Flashing, and Upgrades Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Computer_cooling",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Computer_cooling|Thermal_paste|UEFI|Cable_management|Overclocking&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "pc_maintenance_upgrades_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Thermal interface conduction and firmware maintenance"
        ]
    },
    {
        "domain_id": "38_smartphones_and_mobile_apps",
        "domain_name": "Smartphones and mobile apps",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "38_01",
        "subtopic_name": "Phone specifications and comparisons",
        "candidate_title": "Mobile Technology: Smartphone SoCs, Displays, and Sensors Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Smartphone",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Smartphone|System_on_a_chip|OLED|Camera_sensor|IP_code&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "smartphone_specifications_comparisons_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Heterogeneous mobile silicon and display metrics"
        ]
    },
    {
        "domain_id": "38_smartphones_and_mobile_apps",
        "domain_name": "Smartphones and mobile apps",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "38_02",
        "subtopic_name": "App features and reviews",
        "candidate_title": "Mobile Application Ecosystems: App Store Dynamics and Software Features Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Mobile_app",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Mobile_app|Google_Play|App_Store_(Apple)|In-app_purchase|Push_technology&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "mobile_apps_features_reviews_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Application distribution frameworks and user rating mechanisms"
        ]
    },
    {
        "domain_id": "38_smartphones_and_mobile_apps",
        "domain_name": "Smartphones and mobile apps",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "38_03",
        "subtopic_name": "Battery life and device usage",
        "candidate_title": "Mobile Energy Optimization: Lithium-Ion Degradation and Screen Time Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Lithium-ion_battery",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Lithium-ion_battery|Battery_management_system|Screen_time|Fast_charging|Power_management&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "mobile_battery_usage_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Electrochemical cycle wear and OS background throttling"
        ]
    },
    {
        "domain_id": "38_smartphones_and_mobile_apps",
        "domain_name": "Smartphones and mobile apps",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "38_04",
        "subtopic_name": "Mobile usability and troubleshooting",
        "candidate_title": "Mobile UX Guidelines, Touch Latency, and OS Troubleshooting Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Mobile_operating_system",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Mobile_operating_system|Android_(operating_system)|IOS|Touchscreen|Safe_mode&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "mobile_usability_troubleshooting_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Gesture ergonomics and recovery partition workflows"
        ]
    },
    {
        "domain_id": "39_internet_and_computer_networks",
        "domain_name": "Internet and computer networks",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "39_01",
        "subtopic_name": "Network terminology",
        "candidate_title": "Telecommunications: OSI Model, TCP/IP Suite, and Routing Terminology Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Internet_protocol_suite",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Internet_protocol_suite|OSI_model|Domain_Name_System|IPv6|Subnetwork&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "network_terminology_protocols_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Formal protocol layer models and packet headers"
        ]
    },
    {
        "domain_id": "39_internet_and_computer_networks",
        "domain_name": "Internet and computer networks",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "39_02",
        "subtopic_name": "Internet speed and connectivity",
        "candidate_title": "Broadband Metrics: Throughput, Latency, Jitter, and Packet Loss Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Broadband",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Broadband|Latency_(engineering)|Jitter|Packet_loss|Bandwidth_(computing)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "internet_speed_connectivity_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Network transmission characteristics and bandwidth limits"
        ]
    },
    {
        "domain_id": "39_internet_and_computer_networks",
        "domain_name": "Internet and computer networks",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "39_03",
        "subtopic_name": "Wi-Fi troubleshooting",
        "candidate_title": "Wireless Local Area Networks: 802.11 Protocols and Interference Mitigation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Wi-Fi",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Wi-Fi|IEEE_802.11|Electromagnetic_interference|Wireless_access_point|WPA3&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "wifi_troubleshooting_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Radio frequency channel allocation and encryption"
        ]
    },
    {
        "domain_id": "39_internet_and_computer_networks",
        "domain_name": "Internet and computer networks",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "39_04",
        "subtopic_name": "Network reliability and performance",
        "candidate_title": "Network Engineering: QoS, SLA Uptime, and Diagnostics Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Quality_of_service",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Quality_of_service|Traceroute|Ping_(networking_utility)|Service-level_agreement|High_availability&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "network_reliability_performance_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Packet prioritization algorithms and network diagnostics"
        ]
    },
    {
        "domain_id": "40_artificial_intelligence_and_data_science",
        "domain_name": "Artificial intelligence and data science",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "40_01",
        "subtopic_name": "Machine learning concepts",
        "candidate_title": "Machine Learning Foundations: Supervised, Unsupervised, and Gradient Descent Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Machine_learning",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Machine_learning|Supervised_learning|Overfitting|Gradient_descent|Cross-validation_(statistics)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "machine_learning_concepts_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Statistical learning theory and optimization algorithms"
        ]
    },
    {
        "domain_id": "40_artificial_intelligence_and_data_science",
        "domain_name": "Artificial intelligence and data science",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "40_02",
        "subtopic_name": "Data analysis and interpretation",
        "candidate_title": "Exploratory Data Analysis: Distributions, p-Values, and Causality Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Data_analysis",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Data_analysis|Exploratory_data_analysis|Statistical_hypothesis_testing|P-value|Correlation_does_not_imply_causation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "data_analysis_interpretation_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Inferential statistics and observational study pitfalls"
        ]
    },
    {
        "domain_id": "40_artificial_intelligence_and_data_science",
        "domain_name": "Artificial intelligence and data science",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "40_03",
        "subtopic_name": "AI applications in daily life",
        "candidate_title": "Applied AI: Natural Language Processing, Vision, and Autonomous Systems Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Applications_of_artificial_intelligence",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Applications_of_artificial_intelligence|Natural_language_processing|Computer_vision|Speech_recognition|Autonomous_car&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "ai_applications_daily_life_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Commercial deployments and interactive machine intelligence"
        ]
    },
    {
        "domain_id": "40_artificial_intelligence_and_data_science",
        "domain_name": "Artificial intelligence and data science",
        "category": "Category H \u2014 Technology and digital life",
        "subtopic_id": "40_04",
        "subtopic_name": "AI limitations, reliability, and evaluation",
        "candidate_title": "AI Alignment, Bias, Hallucination, and Benchmark Evaluation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Hallucination_(artificial_intelligence)|Algorithmic_bias|AI_safety|Evaluation_measures_(information_retrieval)|Perplexity&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "ai_limitations_reliability_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Model failure modes and formal evaluation metrics"
        ]
    },
    {
        "domain_id": "41_population_and_demographics",
        "domain_name": "Population and demographics",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "41_01",
        "subtopic_name": "Population growth",
        "candidate_title": "Demography: Global Population Trajectory and Demographic Transition Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Demography",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Demography|Demographic_transition|Total_fertility_rate|Mortality_rate|Overpopulation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "population_growth_demography_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Demographic transition model phases and vital statistics"
        ]
    },
    {
        "domain_id": "41_population_and_demographics",
        "domain_name": "Population and demographics",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "41_02",
        "subtopic_name": "Age distribution",
        "candidate_title": "Population Pyramids, Dependency Ratios, and Demographic Aging Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Population_pyramid",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Population_pyramid|Population_ageing|Dependency_ratio|Baby_boom|Median_age&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "age_distribution_pyramids_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Age cohort distributions and macroeconomic dependency"
        ]
    },
    {
        "domain_id": "41_population_and_demographics",
        "domain_name": "Population and demographics",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "41_03",
        "subtopic_name": "Urbanization and migration",
        "candidate_title": "Human Geography: Urbanization, Megacities, and Rural-Urban Migration Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Urbanization",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Urbanization|Megacity|Human_migration|Rural-urban_fringe|Suburbanization&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "urbanization_migration_geography_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Spatial demographic concentration and mobility"
        ]
    },
    {
        "domain_id": "41_population_and_demographics",
        "domain_name": "Population and demographics",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "41_04",
        "subtopic_name": "Household size and composition",
        "candidate_title": "Family Sociology: Household Composition, Single Living, and Family Structures Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Household",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Household|Nuclear_family|Extended_family|Single-person_household|Cohabitation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "household_size_composition_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Domestic structural evolution in industrial societies"
        ]
    },
    {
        "domain_id": "42_transportation_and_traffic",
        "domain_name": "Transportation and traffic",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "42_01",
        "subtopic_name": "Traffic congestion",
        "candidate_title": "Traffic Engineering: Bottleneck Phenomena, Congestion Pricing, and Flow Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Traffic_congestion",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Traffic_congestion|Traffic_flow|Congestion_pricing|Induced_demand|Gridlock&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "traffic_congestion_engineering_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Hydrodynamic traffic flow models and pricing"
        ]
    },
    {
        "domain_id": "42_transportation_and_traffic",
        "domain_name": "Transportation and traffic",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "42_02",
        "subtopic_name": "Road safety and driving behavior",
        "candidate_title": "Vehicular Safety: Defensive Driving, Collision Analysis, and Restraints Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Road_traffic_safety",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Road_traffic_safety|Defensive_driving|Seat_belt|Speed_limit|Traffic_collision&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "road_safety_driving_behavior_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Passive/active vehicular safety and collision statistics"
        ]
    },
    {
        "domain_id": "42_transportation_and_traffic",
        "domain_name": "Transportation and traffic",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "42_03",
        "subtopic_name": "Public transport services",
        "candidate_title": "Urban Transit Systems: BRT, Metro Rail, and Multimodal Transit Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Public_transport",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Public_transport|Bus_rapid_transit|Rapid_transit|Commuter_rail|Fare_evasion&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "public_transport_services_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Mass transit scheduling and headway engineering"
        ]
    },
    {
        "domain_id": "42_transportation_and_traffic",
        "domain_name": "Transportation and traffic",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "42_04",
        "subtopic_name": "Travel time and route planning",
        "candidate_title": "Algorithmic Route Navigation, Commuting Time, and Isochrones Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Dijkstra%27s_algorithm|Route_assignment|Commuting|Isochrone_map|Turn-by-turn_navigation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "route_planning_navigation_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Graph traversal algorithms and travel impedance functions"
        ]
    },
    {
        "domain_id": "43_emergencies_and_disaster_preparedness",
        "domain_name": "Emergencies and disaster preparedness",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "43_01",
        "subtopic_name": "Fire safety",
        "candidate_title": "Fire Protection Engineering: Extinguishment, Alarms, and Evacuation Plans Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Fire_safety",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Fire_safety|Fire_extinguisher|Smoke_detector|Fire_door|Emergency_evacuation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "fire_safety_evacuation_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Combustion classes and life-safety egress standards"
        ]
    },
    {
        "domain_id": "43_emergencies_and_disaster_preparedness",
        "domain_name": "Emergencies and disaster preparedness",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "43_02",
        "subtopic_name": "Earthquake preparedness",
        "candidate_title": "Seismological Safety: Seismic Retrofitting, Shaking Protocols, and Emergency Kits Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Earthquake_preparedness",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Earthquake_preparedness|Seismic_retrofit|Tsunami_warning_system|Earthquake_engineering|Liquefaction&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "earthquake_preparedness_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Seismic wave mitigation and structural resilience"
        ]
    },
    {
        "domain_id": "43_emergencies_and_disaster_preparedness",
        "domain_name": "Emergencies and disaster preparedness",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "43_03",
        "subtopic_name": "Flood preparedness",
        "candidate_title": "Hydrological Mitigation: Levees, Sump Pumps, and Flood Warning Systems Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Flood_control",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Flood_control|Levee|Flash_flood|Floodplain_management|Sandbag&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "flood_preparedness_control_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Flood basin zoning and hydrological barriers"
        ]
    },
    {
        "domain_id": "43_emergencies_and_disaster_preparedness",
        "domain_name": "Emergencies and disaster preparedness",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "43_04",
        "subtopic_name": "Emergency response procedures",
        "candidate_title": "Civil Protection: Incident Command System, Triage, and 72-Hour Kits Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Incident_Command_System",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Incident_Command_System|Emergency_management|Triage|Disaster_response|Survival_kit&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "emergency_response_procedures_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Standardized emergency response hierarchies and resource management"
        ]
    },
    {
        "domain_id": "44_water_and_sanitation",
        "domain_name": "Water and sanitation",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "44_01",
        "subtopic_name": "Drinking water quality",
        "candidate_title": "Potable Water Engineering: WHO Standards, Contaminants, and Filtration Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Drinking_water_quality_standards",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Drinking_water_quality_standards|Water_purification|Turbidity|Chlorination|Reverse_osmosis&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "drinking_water_quality_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Maximum contaminant levels (MCL) and disinfection chemistry"
        ]
    },
    {
        "domain_id": "44_water_and_sanitation",
        "domain_name": "Water and sanitation",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "44_02",
        "subtopic_name": "Water conservation",
        "candidate_title": "Resource Management: Xeriscaping, Low-Flow Fixtures, and Conservation Policies Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Water_conservation",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Water_conservation|Xeriscaping|Rainwater_harvesting|Greywater|Water_meter&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "water_conservation_management_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Municipal demand reduction and fixture efficiency"
        ]
    },
    {
        "domain_id": "44_water_and_sanitation",
        "domain_name": "Water and sanitation",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "44_03",
        "subtopic_name": "Wastewater and sewage management",
        "candidate_title": "Environmental Engineering: Activated Sludge, Clarification, and Effluents Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Wastewater_treatment",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Wastewater_treatment|Activated_sludge|Septic_tank|Sewage|Biochemical_oxygen_demand&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "wastewater_sewage_management_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Biological oxidation and anaerobic sludge digestion"
        ]
    },
    {
        "domain_id": "44_water_and_sanitation",
        "domain_name": "Water and sanitation",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "44_04",
        "subtopic_name": "Household water consumption",
        "candidate_title": "Residential Hydrology: End-Use Water Breakdown and Leak Detection Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Residential_water_use_in_the_US_and_Canada",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Residential_water_use_in_the_US_and_Canada|Water_footprint|Plumbing_fixture|Smart_water_metering|Water_scarcity&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "household_water_consumption_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Per capita indoor/outdoor usage fractions"
        ]
    },
    {
        "domain_id": "45_housing_and_buildings",
        "domain_name": "Housing and buildings",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "45_01",
        "subtopic_name": "Rental housing and property features",
        "candidate_title": "Property Management: Tenancy Agreements, Rent Regulations, and Amenities Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Renting",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Renting|Lease|Tenant|Landlord|Affordable_housing&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "rental_housing_property_features_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Contractual lease mechanics and housing rights"
        ]
    },
    {
        "domain_id": "45_housing_and_buildings",
        "domain_name": "Housing and buildings",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "45_02",
        "subtopic_name": "Building materials",
        "candidate_title": "Civil Engineering: Structural Materials, Concrete, Steel, and Timber Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Building_material",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Building_material|Concrete|Structural_steel|Timber_framing|Masonry&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "building_materials_engineering_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Compressive/tensile mechanical properties of building components"
        ]
    },
    {
        "domain_id": "45_housing_and_buildings",
        "domain_name": "Housing and buildings",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "45_03",
        "subtopic_name": "Home energy efficiency",
        "candidate_title": "Building Physics: Thermal Envelopes, Insulation, and Net-Zero Energy Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Low-energy_house",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Low-energy_house|Building_insulation|R-value_(insulation)|Heat_pump|Zero-energy_building&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "home_energy_efficiency_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Thermal transmission coefficients and envelope sealing"
        ]
    },
    {
        "domain_id": "45_housing_and_buildings",
        "domain_name": "Housing and buildings",
        "category": "Category I \u2014 Society, public services, and infrastructure",
        "subtopic_id": "45_04",
        "subtopic_name": "Maintenance and repair planning",
        "candidate_title": "Facility Management: Preventative Lifecycle Schedules and Structural Inspection Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Facility_management",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Facility_management|Planned_maintenance|Roof|Structural_integrity_and_failure|Condition_monitoring&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "building_maintenance_repair_planning_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Asset depreciation schedules and architectural inspection"
        ]
    },
    {
        "domain_id": "46_travel_and_tourism",
        "domain_name": "Travel and tourism",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "46_01",
        "subtopic_name": "Destination descriptions",
        "candidate_title": "Tourism Geography: World Heritage Sites, Eco-Tourism, and Landmarks Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Tourism",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Tourism|World_Heritage_Site|Ecotourism|Cultural_tourism|Tourist_attraction&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "tourism_destination_descriptions_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Geographic destination profiles and cultural heritage"
        ]
    },
    {
        "domain_id": "46_travel_and_tourism",
        "domain_name": "Travel and tourism",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "46_02",
        "subtopic_name": "Travel budgets and itineraries",
        "candidate_title": "Travel Logistics: Backpacker Budgeting, Itinerary Structuring, and Passes Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Backpacking_(travel)",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Backpacking_(travel)|Itinerary|Travel_agency|Eurail|Travel_technology&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "travel_budgets_itineraries_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Transit budgeting and route planning logistics"
        ]
    },
    {
        "domain_id": "46_travel_and_tourism",
        "domain_name": "Travel and tourism",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "46_03",
        "subtopic_name": "Accommodation comparisons",
        "candidate_title": "Hospitality Management: Hotels, Hostels, and Short-Term Rental Models Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Hotel",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Hotel|Hostel|Bed_and_breakfast|Short-term_rental|Hospitality_industry&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "accommodation_comparisons_hospitality.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Lodging classifications and amenity benchmarking"
        ]
    },
    {
        "domain_id": "46_travel_and_tourism",
        "domain_name": "Travel and tourism",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "46_04",
        "subtopic_name": "Travel reviews and visitor experiences",
        "candidate_title": "Traveler Experience Studies, Cultural Tourism, and Review Systems Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Tripadvisor",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Tripadvisor|Online_travel_agency|Culture_shock|Travel_behavior|Tourist_gaze&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "travel_reviews_visitor_experiences.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Ethnographic visitor perception and peer review heuristics"
        ]
    },
    {
        "domain_id": "47_languages_and_communication",
        "domain_name": "Languages and communication",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "47_01",
        "subtopic_name": "Vocabulary and word meanings",
        "candidate_title": "Linguistic Semantics, Lexicology, and WordNet Synsets Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Lexical_semantics",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Lexical_semantics|Synonym|Etymology|Morphology_(linguistics)|WordNet&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "vocabulary_word_meanings_semantics.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Semantic relational taxonomies and etymological roots"
        ]
    },
    {
        "domain_id": "47_languages_and_communication",
        "domain_name": "Languages and communication",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "47_02",
        "subtopic_name": "Grammar and sentence structure",
        "candidate_title": "Theoretical Syntax, Generative Grammar, and Dependency Trees Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Syntax",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Syntax|Grammar|Clause|Subject%E2%80%93verb%E2%80%93object|Universal_grammar&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "grammar_sentence_structure_syntax.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Syntactic constituency and grammatical inflections"
        ]
    },
    {
        "domain_id": "47_languages_and_communication",
        "domain_name": "Languages and communication",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "47_03",
        "subtopic_name": "Translation and paraphrasing",
        "candidate_title": "Translation Studies: Semantic Equivalence, Idioms, and Machine Translation Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Translation",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Translation|Machine_translation|Paraphrase|Idiom|BLEU&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "translation_paraphrasing_studies_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Cross-lingual fidelity and idiomatic adaptation"
        ]
    },
    {
        "domain_id": "47_languages_and_communication",
        "domain_name": "Languages and communication",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "47_04",
        "subtopic_name": "Written communication and comprehension",
        "candidate_title": "Rhetoric, Discourse Analysis, and Written Communication Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Rhetoric",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Rhetoric|Discourse_analysis|Reading_comprehension|Expository_writing|Cohesion_(linguistics)&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "written_communication_comprehension_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Rhetorical appeals and structural textual cohesion"
        ]
    },
    {
        "domain_id": "48_human_behavior_and_psychology",
        "domain_name": "Human behavior and psychology",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "48_01",
        "subtopic_name": "Decision-making",
        "candidate_title": "Behavioral Economics: Heuristics, Prospect Theory, and Biases Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Decision-making",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Decision-making|Prospect_theory|Heuristics_in_judgment_and_decision-making|Cognitive_bias|Bounded_rationality&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "decision_making_behavioral_economics.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "System 1 and System 2 cognitive processing frameworks"
        ]
    },
    {
        "domain_id": "48_human_behavior_and_psychology",
        "domain_name": "Human behavior and psychology",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "48_02",
        "subtopic_name": "Memory and attention",
        "candidate_title": "Cognitive Psychology: Working Memory, Consolidation, and Attention Span Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Memory",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Memory|Working_memory|Attention|Long-term_memory|Forgetting_curve&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "memory_attention_cognitive_psychology.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Atkinson-Shiffrin models and selective attentional filters"
        ]
    },
    {
        "domain_id": "48_human_behavior_and_psychology",
        "domain_name": "Human behavior and psychology",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "48_03",
        "subtopic_name": "Motivation and habits",
        "candidate_title": "Motivation Theories: Self-Determination, Extrinsic Rewards, and Drive Theory Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Motivation",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Motivation|Self-determination_theory|Maslow%27s_hierarchy_of_needs|Extrinsic_motivation|Intrinsic_motivation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "motivation_habits_psychology_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Psychological needs and goal-directed human action"
        ]
    },
    {
        "domain_id": "48_human_behavior_and_psychology",
        "domain_name": "Human behavior and psychology",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "48_04",
        "subtopic_name": "Social interaction and group behavior",
        "candidate_title": "Social Psychology: Group Polarization, Conformity, and Bystander Effect Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Social_psychology",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Social_psychology|Asch_conformity_experiments|Bystander_effect|Groupthink|In-group_and_out-group&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "social_interaction_group_behavior.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Normative social influence and collective dynamics"
        ]
    },
    {
        "domain_id": "49_relationships_and_family_life",
        "domain_name": "Relationships and family life",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "49_01",
        "subtopic_name": "Family communication",
        "candidate_title": "Interpersonal Communication: Family Systems and Empathic Dialogue Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Interpersonal_communication",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Interpersonal_communication|Active_listening|Family_systems_theory|Nonviolent_Communication|Assertiveness&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "family_communication_interpersonal_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Systemic familial patterns and nonviolent verbal structures"
        ]
    },
    {
        "domain_id": "49_relationships_and_family_life",
        "domain_name": "Relationships and family life",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "49_02",
        "subtopic_name": "Conflict resolution",
        "candidate_title": "Conflict De-escalation: Principled Negotiation, Mediation, and Compromise Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Conflict_resolution",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Conflict_resolution|Mediation|Negotiation|De-escalation|Forgiveness&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "conflict_resolution_mediation_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Harvard negotiation project and mediation protocols"
        ]
    },
    {
        "domain_id": "49_relationships_and_family_life",
        "domain_name": "Relationships and family life",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "49_03",
        "subtopic_name": "Parenting and child development",
        "candidate_title": "Developmental Psychology: Attachment Theory, Parenting Styles, and Milestones Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Parenting",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Parenting|Attachment_theory|Child_development|Parenting_styles|Piaget%27s_theory_of_cognitive_development&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "parenting_child_development_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Authoritative parenting and psychosocial stages of development"
        ]
    },
    {
        "domain_id": "49_relationships_and_family_life",
        "domain_name": "Relationships and family life",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "49_04",
        "subtopic_name": "Cooperation and interpersonal skills",
        "candidate_title": "Prosocial Psychology: Reciprocity, Empathy, and Cooperative Problem Solving Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Prosocial_behavior",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Prosocial_behavior|Empathy|Altruism|Reciprocity_(social_psychology)|Cooperation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "cooperation_interpersonal_skills_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Evolutionary biology of mutual aid and interpersonal empathy"
        ]
    },
    {
        "domain_id": "50_non_political_news_and_current_events",
        "domain_name": "Non-political news and current events",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "50_01",
        "subtopic_name": "Science and technology developments",
        "candidate_title": "Science & Technology Journalism: Breakthroughs and Discoveries Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Science_journalism",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Science_journalism|James_Webb_Space_Telescope|Quantum_computing|Renewable_energy|CRISPR&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "science_tech_news_developments_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Non-political empirical reporting on scientific research"
        ]
    },
    {
        "domain_id": "50_non_political_news_and_current_events",
        "domain_name": "Non-political news and current events",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "50_02",
        "subtopic_name": "Environmental and weather reports",
        "candidate_title": "Environmental Meteorology Reports: Ocean Anomaly and Ice Extent Updates Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Environmental_journalism",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Environmental_journalism|Weather_forecasting|Sea_ice|Ocean_temperature|Deforestation&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "environmental_weather_reports_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Empirical meteorological and ecological event updates"
        ]
    },
    {
        "domain_id": "50_non_political_news_and_current_events",
        "domain_name": "Non-political news and current events",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "50_03",
        "subtopic_name": "Sports news and match reports",
        "candidate_title": "Sports Journalism: Athletic Tournaments and Championship Dispatches Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Sports_journalism",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Sports_journalism|Olympic_Games|World_Athletics_Championships|Paralympic_Games|Sports_broadcasting&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "sports_news_match_reports_corpus.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Tournament recaps and athletic records reporting"
        ]
    },
    {
        "domain_id": "50_non_political_news_and_current_events",
        "domain_name": "Non-political news and current events",
        "category": "Category J \u2014 Travel, communication, and human behavior",
        "subtopic_id": "50_04",
        "subtopic_name": "Health, education, and community announcements",
        "candidate_title": "Public Health & Community Education Announcements Corpus",
        "source_platform": "Wikimedia Foundation",
        "publisher": "Wikimedia Foundation Contributor Community",
        "source_url": "https://en.wikipedia.org/wiki/Public_health",
        "download_url": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Public_health|Health_literacy|Open_educational_resources|Community_health|Public_library&format=json",
        "license": "CC-BY-SA 4.0",
        "language": "en",
        "format": "json",
        "target_filename": "health_education_community_announcements.json",
        "text_fields": [
            "title",
            "extract"
        ],
        "limitations": [
            "Civic education notices and community health directives"
        ]
    }
]
