#!/usr/bin/env python3
"""
run_category_a.py - Downloads and registers high-capacity raw text for Category A:
- 01_education_and_studying
- 02_general_knowledge
- 03_mathematics
- 04_physics_and_chemistry
- 05_space_and_the_universe
"""

import os
import sys
import time
from expand_corpus_engine import (
    save_and_register_dataset,
    download_direct_file,
    fetch_wikipedia_corpus
)

def run_category_a():
    print("=" * 70)
    print("STARTING EXPANSION: CATEGORY A (Domains 01 - 05)")
    print("=" * 70)
    t0 = time.time()
    total_bytes = 0

    # -------------------------------------------------------------------------
    # DOMAIN 01: EDUCATION AND STUDYING
    # -------------------------------------------------------------------------
    print("\n>>> Expanding 01_education_and_studying...")
    
    # 01_04: SQuAD Reading Comprehension Benchmark Shard (Stanford NLP)
    try:
        print("  - Downloading SQuAD v1.1 Reading Comprehension Train JSON...")
        data = download_direct_file("https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json")
        sz = save_and_register_dataset(
            domain_id="01_education_and_studying",
            domain_name="Education and Studying",
            subtopic_id="01_04",
            subtopic_slug="academic_performance_and_study_habits",
            subtopic_name="Academic Performance & Study Habits",
            source_slug="stanford_squad_reading_comprehension",
            filename="stanford_squad_v1_reading_comprehension_train.json",
            content_bytes=data,
            candidate_title="Stanford Question Answering Dataset (SQuAD v1.1) Reading Comprehension Corpus",
            source_platform="Hugging Face / Stanford NLP",
            publisher="Stanford University NLP Group (Rajpurkar et al.)",
            source_url="https://rajpurkar.github.io/SQuAD-explorer/",
            download_url="https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json",
            license_type="CC BY-SA 4.0",
            format_type="json",
            description="Official train split of the SQuAD 1.1 benchmark containing 100,000+ reading comprehension questions and human-written answer passages on diverse educational and academic topics."
        )
        total_bytes += sz
        print(f"    Saved SQuAD v1.1: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] SQuAD v1.1 download failed: {e}")

    # 01_04: SciQ Science Exam Question Answering Benchmark Parquet (Allen AI)
    try:
        print("  - Downloading SciQ Science Exam QA Parquet (Allen AI)...")
        data = download_direct_file("https://huggingface.co/datasets/allenai/sciq/resolve/main/data/train-00000-of-00001.parquet")
        sz = save_and_register_dataset(
            domain_id="01_education_and_studying",
            domain_name="Education and Studying",
            subtopic_id="01_04",
            subtopic_slug="academic_performance_and_study_habits",
            subtopic_name="Academic Performance & Study Habits",
            source_slug="allenai_sciq_exam_questions",
            filename="allenai_sciq_science_exam_questions_train.parquet",
            content_bytes=data,
            candidate_title="SciQ Science Examination Question Answering Benchmark Corpus",
            source_platform="Hugging Face",
            publisher="Allen Institute for AI (AllenAI)",
            source_url="https://huggingface.co/datasets/allenai/sciq",
            download_url="https://huggingface.co/datasets/allenai/sciq/resolve/main/data/train-00000-of-00001.parquet",
            license_type="CC BY-NC 3.0",
            format_type="parquet",
            description="Science exam question answering dataset containing 13,679 multiple choice questions across physics, chemistry, biology, and earth science with detailed textual explanations."
        )
        total_bytes += sz
        print(f"    Saved SciQ: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] SciQ download failed: {e}")

    # 01_01: Maria Montessori The Montessori Method (pg34110)
    try:
        print("  - Downloading Maria Montessori: The Montessori Method...")
        data = download_direct_file("https://www.gutenberg.org/cache/epub/34110/pg34110.txt")
        sz = save_and_register_dataset(
            domain_id="01_education_and_studying",
            domain_name="Education and Studying",
            subtopic_id="01_01",
            subtopic_slug="study_techniques_and_learning_strategies",
            subtopic_name="Study Techniques & Learning Strategies",
            source_slug="project_gutenberg_maria_montessori_the_montessori_method",
            filename="maria_montessori_the_montessori_method_complete.txt",
            content_bytes=data,
            candidate_title="The Montessori Method: Scientific Pedagogy as Applied to Child Education",
            source_platform="Project Gutenberg",
            publisher="Maria Montessori (Project Gutenberg Release)",
            source_url="https://www.gutenberg.org/ebooks/34110",
            download_url="https://www.gutenberg.org/cache/epub/34110/pg34110.txt",
            license_type="Public Domain",
            format_type="txt",
            description="Complete unabridged English translation of Maria Montessori's foundational pedagogical treatise on student-centered learning, tactile education, and focused study habits."
        )
        total_bytes += sz
        print(f"    Saved Montessori: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Montessori download failed: {e}")

    # 01 Wikipedia Deep Corpus
    wiki_01_titles = [
        "Study_skills", "Spaced_repetition", "Active_recall", "Mnemonic", "Pomodoro_Technique",
        "Cognitive_load", "Retrieval_practice", "Mind_map", "Note-taking", "Cornell_Notes",
        "Dual-coding_theory", "Metacognition", "Chunking_(psychology)", "Memory_span", "Working_memory",
        "Flashcard", "Leitner_system", "SQ3R", "Elaborative_rehearsal", "Learning_styles",
        "Test_preparation", "Standardized_test", "Cramming_(education)", "Practice_effect",
        "Formative_assessment", "Summative_assessment", "Test_anxiety", "SAT", "ACT_(test)",
        "Advanced_Placement", "International_Baccalaureate", "Graduate_Record_Examinations",
        "Medical_College_Admission_Test", "Law_School_Admission_Test", "Multiple-choice", "Rubric_(academic)",
        "Grading_in_education", "Testing_effect", "Academic_grading_in_the_United_States",
        "Time_management", "Procrastination", "Eisenhower_Matrix", "Getting_Things_Done",
        "Time_blocking", "Habit", "Productivity", "Goal_setting", "Self-regulated_learning",
        "Academic_integrity", "Syllabus", "Homework", "Occupational_burnout", "Attention_span",
        "Flow_(psychology)", "Willpower", "Self-control", "Academic_achievement",
        "Intelligence_quotient", "Growth_mindset", "Peer_group", "Educational_psychology"
    ]
    print(f"  - Fetching {len(wiki_01_titles)} Wikipedia education articles...")
    data, titles = fetch_wikipedia_corpus(wiki_01_titles)
    sz = save_and_register_dataset(
        domain_id="01_education_and_studying",
        domain_name="Education and Studying",
        subtopic_id="01_03",
        subtopic_slug="student_time_management",
        subtopic_name="Student Time Management",
        source_slug="wikimedia_foundation_comprehensive_pedagogy_corpus",
        filename="wikimedia_foundation_comprehensive_pedagogy_and_study_corpus.txt",
        content_bytes=data,
        candidate_title="Wikimedia Comprehensive Pedagogy, Cognitive Learning & Study Habits Corpus",
        source_platform="Wikimedia Foundation",
        publisher="Wikipedia Contributors",
        source_url="https://en.wikipedia.org/wiki/Special:Export",
        download_url="https://en.wikipedia.org/w/api.php",
        license_type="CC BY-SA 4.0 / GFDL",
        format_type="txt",
        description=f"Curated full-text revision corpus spanning {len(titles)} comprehensive encyclopedic articles on pedagogy, student time management, cognitive load, memory retention, and educational assessment."
    )
    total_bytes += sz
    print(f"    Saved Education Wikipedia Corpus: {sz / (1024*1024):.2f} MB ({len(titles)} articles)")

    # -------------------------------------------------------------------------
    # DOMAIN 02: GENERAL KNOWLEDGE
    # -------------------------------------------------------------------------
    print("\n>>> Expanding 02_general_knowledge...")
    
    # 02_04: Wikitext-2 Raw Train Parquet (Hugging Face)
    try:
        print("  - Downloading Wikitext-2 Raw Train Parquet...")
        data = download_direct_file("https://huggingface.co/datasets/wikitext/resolve/main/wikitext-2-raw-v1/train-00000-of-00001.parquet")
        sz = save_and_register_dataset(
            domain_id="02_general_knowledge",
            domain_name="General Knowledge",
            subtopic_id="02_04",
            subtopic_slug="everyday_facts_about_the_world",
            subtopic_name="Everyday Facts About the World",
            source_slug="hugging_face_wikitext_2_raw_corpus",
            filename="wikitext_2_raw_train_articles_corpus.parquet",
            content_bytes=data,
            candidate_title="Wikitext-2 Raw Language Modeling and Fact Benchmark Corpus",
            source_platform="Hugging Face",
            publisher="Salesforce Research (Merity et al.)",
            source_url="https://huggingface.co/datasets/wikitext",
            download_url="https://huggingface.co/datasets/wikitext/resolve/main/wikitext-2-raw-v1/train-00000-of-00001.parquet",
            license_type="CC BY-SA 3.0",
            format_type="parquet",
            description="Standard NLP benchmark consisting of 2+ million tokens extracted from the set of verified Good and Featured articles on Wikipedia."
        )
        total_bytes += sz
        print(f"    Saved Wikitext-2: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Wikitext-2 download failed: {e}")

    # 02_01: Gibbon Decline & Fall Vol 2 (pg25718)
    try:
        print("  - Downloading Edward Gibbon: Decline and Fall of the Roman Empire Vol 2...")
        data = download_direct_file("https://www.gutenberg.org/cache/epub/25718/pg25718.txt")
        sz = save_and_register_dataset(
            domain_id="02_general_knowledge",
            domain_name="General Knowledge",
            subtopic_id="02_01",
            subtopic_slug="historical_civilizations",
            subtopic_name="Historical Civilizations",
            source_slug="project_gutenberg_edward_gibbon_decline_and_fall_vol2",
            filename="edward_gibbon_decline_and_fall_roman_empire_vol2.txt",
            content_bytes=data,
            candidate_title="The History of the Decline and Fall of the Roman Empire (Volume II)",
            source_platform="Project Gutenberg",
            publisher="Edward Gibbon (Project Gutenberg Release)",
            source_url="https://www.gutenberg.org/ebooks/25718",
            download_url="https://www.gutenberg.org/cache/epub/25718/pg25718.txt",
            license_type="Public Domain",
            format_type="txt",
            description="Complete unabridged Volume II of Edward Gibbon's masterwork on the history, political structures, and civil institutions of classical antiquity."
        )
        total_bytes += sz
        print(f"    Saved Gibbon Vol 2: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Gibbon download failed: {e}")

    # 02_03: Marco Polo The Travels of Marco Polo (pg10636)
    try:
        print("  - Downloading Marco Polo: The Travels of Marco Polo...")
        data = download_direct_file("https://www.gutenberg.org/cache/epub/10636/pg10636.txt")
        sz = save_and_register_dataset(
            domain_id="02_general_knowledge",
            domain_name="General Knowledge",
            subtopic_id="02_03",
            subtopic_slug="world_geography",
            subtopic_name="World Geography",
            source_slug="project_gutenberg_marco_polo_the_travels",
            filename="marco_polo_the_travels_of_marco_polo_complete.txt",
            content_bytes=data,
            candidate_title="The Travels of Marco Polo: Descriptive Accounts of Medieval Asian Geography",
            source_platform="Project Gutenberg",
            publisher="Marco Polo / Rustichello da Pisa (Project Gutenberg Release)",
            source_url="https://www.gutenberg.org/ebooks/10636",
            download_url="https://www.gutenberg.org/cache/epub/10636/pg10636.txt",
            license_type="Public Domain",
            format_type="txt",
            description="Complete English translation of Marco Polo's historic 13th-century travelogue documenting Eurasian geography, cultures, cities, and trade routes."
        )
        total_bytes += sz
        print(f"    Saved Marco Polo: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Marco Polo download failed: {e}")

    # 02 Wikipedia Deep Corpus
    wiki_02_titles = [
        "Ancient_Egypt", "Roman_Empire", "Ancient_Greece", "Indus_Valley_Civilisation",
        "Han_dynasty", "Byzantine_Empire", "Ottoman_Empire", "Maya_civilization",
        "Aztec_Empire", "Inca_Empire", "Mesopotamia", "Achaemenid_Empire", "Mongol_Empire",
        "Tang_dynasty", "Song_dynasty", "Holy_Roman_Empire", "British_Empire", "Kingdom_of_Kush",
        "Carthage", "Classical_antiquity", "History_of_science", "Industrial_Revolution",
        "Printing_press", "Steam_engine", "Compass", "Gunpowder", "Electricity",
        "Telephone", "Transistor", "Penicillin", "Internet", "Automobile", "Incandescent_light_bulb",
        "Vaccination", "Microscope", "Telescope", "Wheel", "Semiconductor", "Radio", "Airplane",
        "Geography", "Physical_geography", "Human_geography", "Plate_tectonics", "Continent",
        "Pacific_Ocean", "Atlantic_Ocean", "Sahara", "Amazon_basin", "Himalayas", "Andes",
        "Nile", "Amazon_River", "Yangtze", "Mississippi_River", "Arctic", "Antarctica",
        "General_knowledge", "Trivia", "World_Heritage_Site", "Seven_Wonders_of_the_Ancient_World",
        "International_System_of_Units", "Coordinated_Universal_Time", "Prime_meridian", "Equator"
    ]
    print(f"  - Fetching {len(wiki_02_titles)} Wikipedia general knowledge articles...")
    data, titles = fetch_wikipedia_corpus(wiki_02_titles)
    sz = save_and_register_dataset(
        domain_id="02_general_knowledge",
        domain_name="General Knowledge",
        subtopic_id="02_02",
        subtopic_slug="discoveries_and_inventions",
        subtopic_name="Discoveries & Inventions",
        source_slug="wikimedia_foundation_world_civilizations_and_inventions",
        filename="wikimedia_foundation_world_civilizations_and_inventions_corpus.txt",
        content_bytes=data,
        candidate_title="Wikimedia Comprehensive Civilizations, Inventions & Geography Corpus",
        source_platform="Wikimedia Foundation",
        publisher="Wikipedia Contributors",
        source_url="https://en.wikipedia.org/wiki/Special:Export",
        download_url="https://en.wikipedia.org/w/api.php",
        license_type="CC BY-SA 4.0 / GFDL",
        format_type="txt",
        description=f"Curated full-text revision corpus spanning {len(titles)} comprehensive encyclopedic articles on world civilizations, major technological discoveries, global physical geography, and universal facts."
    )
    total_bytes += sz
    print(f"    Saved Gen Knowledge Wikipedia Corpus: {sz / (1024*1024):.2f} MB ({len(titles)} articles)")

    # -------------------------------------------------------------------------
    # DOMAIN 03: MATHEMATICS
    # -------------------------------------------------------------------------
    print("\n>>> Expanding 03_mathematics...")

    # 03_02: Rouse Ball History of Mathematics (pg31246)
    try:
        print("  - Downloading W. W. Rouse Ball: A Short Account of the History of Mathematics...")
        data = download_direct_file("https://www.gutenberg.org/cache/epub/31246/pg31246.txt")
        sz = save_and_register_dataset(
            domain_id="03_mathematics",
            domain_name="Mathematics",
            subtopic_id="03_02",
            subtopic_slug="geometry_and_measurements",
            subtopic_name="Geometry & Measurements",
            source_slug="project_gutenberg_w_w_rouse_ball_history_of_mathematics",
            filename="w_w_rouse_ball_history_of_mathematics_complete.txt",
            content_bytes=data,
            candidate_title="A Short Account of the History of Mathematics",
            source_platform="Project Gutenberg",
            publisher="W. W. Rouse Ball (Project Gutenberg Release)",
            source_url="https://www.gutenberg.org/ebooks/31246",
            download_url="https://www.gutenberg.org/cache/epub/31246/pg31246.txt",
            license_type="Public Domain",
            format_type="txt",
            description="Comprehensive unabridged history of pure and applied mathematics covering Greek geometry, Arabic algebra, the calculus revolution, and modern mathematical theories."
        )
        total_bytes += sz
        print(f"    Saved Rouse Ball History of Math: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Rouse Ball download failed: {e}")

    # 03_03: Karl Pearson The Grammar of Science (pg39819)
    try:
        print("  - Downloading Karl Pearson: The Grammar of Science...")
        data = download_direct_file("https://www.gutenberg.org/cache/epub/39819/pg39819.txt")
        sz = save_and_register_dataset(
            domain_id="03_mathematics",
            domain_name="Mathematics",
            subtopic_id="03_03",
            subtopic_slug="statistics_and_probability",
            subtopic_name="Statistics & Probability",
            source_slug="project_gutenberg_karl_pearson_the_grammar_of_science",
            filename="karl_pearson_the_grammar_of_science_complete.txt",
            content_bytes=data,
            candidate_title="The Grammar of Science: Classical Treatise on Statistics & Empirical Science",
            source_platform="Project Gutenberg",
            publisher="Karl Pearson (Project Gutenberg Release)",
            source_url="https://www.gutenberg.org/ebooks/39819",
            download_url="https://www.gutenberg.org/cache/epub/39819/pg39819.txt",
            license_type="Public Domain",
            format_type="txt",
            description="Foundational treatise by mathematical statistician Karl Pearson establishing modern empirical statistical methods, contingency tables, correlation theory, and scientific probability."
        )
        total_bytes += sz
        print(f"    Saved Karl Pearson: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Karl Pearson download failed: {e}")

    # 03_04: Bertrand Russell The Principles of Mathematics (pg2529)
    try:
        print("  - Downloading Bertrand Russell: The Principles of Mathematics...")
        data = download_direct_file("https://www.gutenberg.org/cache/epub/2529/pg2529.txt")
        sz = save_and_register_dataset(
            domain_id="03_mathematics",
            domain_name="Mathematics",
            subtopic_id="03_04",
            subtopic_slug="applied_mathematics_and_problem_solving",
            subtopic_name="Applied Mathematics & Problem Solving",
            source_slug="project_gutenberg_bertrand_russell_principles_of_mathematics",
            filename="bertrand_russell_principles_of_mathematics_complete.txt",
            content_bytes=data,
            candidate_title="The Principles of Mathematics: Foundational Logic & Mathematical Proofs",
            source_platform="Project Gutenberg",
            publisher="Bertrand Russell (Project Gutenberg Release)",
            source_url="https://www.gutenberg.org/ebooks/2529",
            download_url="https://www.gutenberg.org/cache/epub/2529/pg2529.txt",
            license_type="Public Domain",
            format_type="txt",
            description="Masterwork of mathematical logic presenting Russell's reduction of mathematics to symbolic logic, set theory, axiomatic number theory, and rigorous proof mechanisms."
        )
        total_bytes += sz
        print(f"    Saved Bertrand Russell: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Bertrand Russell download failed: {e}")

    # 03 Wikipedia Deep Corpus
    wiki_03_titles = [
        "Abstract_algebra", "Linear_algebra", "Quadratic_equation", "Polynomial", "Group_theory",
        "Ring_(mathematics)", "Field_(mathematics)", "Vector_space", "Matrix_(mathematics)",
        "Determinant", "Eigenvalues_and_eigenvectors", "System_of_linear_equations", "Galois_theory",
        "Fundamental_theorem_of_algebra", "Commutative_algebra", "Lie_algebra", "Boolean_algebra",
        "Euclidean_geometry", "Non-Euclidean_geometry", "Differential_geometry", "Topology",
        "Trigonometry", "Pythagorean_theorem", "Analytic_geometry", "Manifold", "Curvature",
        "Polyhedron", "Sphere", "Cylinder", "Hyperbolic_geometry", "Coordinate_system", "Fractal",
        "Probability_theory", "Statistics", "Normal_distribution", "Central_limit_theorem",
        "Bayes'_theorem", "Random_variable", "Statistical_hypothesis_testing", "P-value",
        "Variance", "Standard_deviation", "Regression_analysis", "Markov_chain", "Monte_Carlo_method",
        "Poisson_distribution", "Law_of_large_numbers", "Confidence_interval", "Chi-squared_distribution",
        "Correlation", "Maximum_likelihood_estimation", "Stochastic_process", "Applied_mathematics",
        "Mathematical_optimization", "Numerical_analysis", "Differential_equation", "Dynamical_system",
        "Calculus_of_variations", "Game_theory", "Operations_research", "Mathematical_physics",
        "Fluid_dynamics", "Cryptography", "Graph_theory", "Fourier_analysis", "Finite_element_method",
        "Information_theory", "Chaos_theory", "Complex_analysis"
    ]
    print(f"  - Fetching {len(wiki_03_titles)} Wikipedia mathematics articles...")
    data, titles = fetch_wikipedia_corpus(wiki_03_titles)
    sz = save_and_register_dataset(
        domain_id="03_mathematics",
        domain_name="Mathematics",
        subtopic_id="03_01",
        subtopic_slug="algebra_and_equations",
        subtopic_name="Algebra & Equations",
        source_slug="wikimedia_foundation_pure_and_applied_mathematics",
        filename="wikimedia_foundation_pure_and_applied_mathematics_corpus.txt",
        content_bytes=data,
        candidate_title="Wikimedia Comprehensive Pure & Applied Mathematics Corpus",
        source_platform="Wikimedia Foundation",
        publisher="Wikipedia Contributors",
        source_url="https://en.wikipedia.org/wiki/Special:Export",
        download_url="https://en.wikipedia.org/w/api.php",
        license_type="CC BY-SA 4.0 / GFDL",
        format_type="txt",
        description=f"Curated full-text revision corpus spanning {len(titles)} comprehensive encyclopedic articles on abstract algebra, differential geometry, topology, mathematical statistics, probability theory, and numerical optimization."
    )
    total_bytes += sz
    print(f"    Saved Mathematics Wikipedia Corpus: {sz / (1024*1024):.2f} MB ({len(titles)} articles)")

    # -------------------------------------------------------------------------
    # DOMAIN 04: PHYSICS AND CHEMISTRY
    # -------------------------------------------------------------------------
    print("\n>>> Expanding 04_physics_and_chemistry...")

    # 04_02: Michael Faraday Experimental Researches in Electricity Vol 1 (pg14986)
    try:
        print("  - Downloading Michael Faraday: Experimental Researches in Electricity Vol 1...")
        data = download_direct_file("https://www.gutenberg.org/cache/epub/14986/pg14986.txt")
        sz = save_and_register_dataset(
            domain_id="04_physics_and_chemistry",
            domain_name="Physics and Chemistry",
            subtopic_id="04_02",
            subtopic_slug="electricity_and_magnetism",
            subtopic_name="Electricity & Magnetism",
            source_slug="project_gutenberg_michael_faraday_electricity_vol1",
            filename="michael_faraday_experimental_researches_electricity_vol1.txt",
            content_bytes=data,
            candidate_title="Experimental Researches in Electricity (Volume I)",
            source_platform="Project Gutenberg",
            publisher="Michael Faraday (Project Gutenberg Release)",
            source_url="https://www.gutenberg.org/ebooks/14986",
            download_url="https://www.gutenberg.org/cache/epub/14986/pg14986.txt",
            license_type="Public Domain",
            format_type="txt",
            description="Primary experimental papers of Michael Faraday establishing electromagnetic induction, magnetic rotation, lines of force, and electrochemical decomposition."
        )
        total_bytes += sz
        print(f"    Saved Faraday Electricity: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Faraday download failed: {e}")

    # 04_04: John Tyndall Heat as a Mode of Motion (pg40974)
    try:
        print("  - Downloading John Tyndall: Heat Considered as a Mode of Motion...")
        data = download_direct_file("https://www.gutenberg.org/cache/epub/40974/pg40974.txt")
        sz = save_and_register_dataset(
            domain_id="04_physics_and_chemistry",
            domain_name="Physics and Chemistry",
            subtopic_id="04_04",
            subtopic_slug="materials_and_their_properties",
            subtopic_name="Materials & Their Properties",
            source_slug="project_gutenberg_john_tyndall_heat_mode_of_motion",
            filename="john_tyndall_heat_considered_mode_of_motion_complete.txt",
            content_bytes=data,
            candidate_title="Heat Considered as a Mode of Motion: Foundational Thermodynamics",
            source_platform="Project Gutenberg",
            publisher="John Tyndall (Project Gutenberg Release)",
            source_url="https://www.gutenberg.org/ebooks/40974",
            download_url="https://www.gutenberg.org/cache/epub/40974/pg40974.txt",
            license_type="Public Domain",
            format_type="txt",
            description="Classic physical treatise on molecular physics, radiant heat absorption, greenhouse gas properties of atmospheric vapors, and mechanical equivalents of heat."
        )
        total_bytes += sz
        print(f"    Saved John Tyndall: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Tyndall download failed: {e}")

    # 04 Wikipedia Deep Corpus
    wiki_04_titles = [
        "Classical_mechanics", "Newton's_laws_of_motion", "Kinetic_energy", "Potential_energy",
        "Conservation_of_energy", "Momentum", "Angular_momentum", "Torque", "Gravitation",
        "Work_(physics)", "Power_(physics)", "Friction", "Harmonic_oscillator", "Inertia",
        "Special_relativity", "General_relativity", "Thermodynamics", "Laws_of_thermodynamics",
        "Entropy", "Heat_transfer", "Electromagnetism", "Electric_charge", "Coulomb's_law",
        "Electric_field", "Magnetic_field", "Maxwell's_equations", "Electromagnetic_radiation",
        "Lorentz_force", "Faraday's_law_of_induction", "Ampère's_circuital_law", "Gauss's_law",
        "Inductance", "Capacitance", "Electric_current", "Voltage", "Electrical_resistance_and_conductance",
        "Ohm's_law", "Alternating_current", "Direct_current", "Superconductivity",
        "Chemical_reaction", "Stoichiometry", "Chemical_equilibrium", "Catalysis",
        "Acid–base_reaction", "Redox", "Combustion", "Exothermic_process", "Endothermic_process",
        "Chemical_kinetics", "Activation_energy", "Reaction_mechanism", "Thermochemistry",
        "Electrochemistry", "Chemical_synthesis", "Enzyme_catalysis", "Le_Chatelier's_principle",
        "Chemical_bond", "Materials_science", "Condensed_matter_physics", "Crystal_structure",
        "Polymer", "Semiconductor", "Metal", "Ceramic", "Composite_material", "Elasticity_(physics)",
        "Tensile_strength", "Hardness", "Thermal_conductivity", "Phase_transition", "Superfluidity"
    ]
    print(f"  - Fetching {len(wiki_04_titles)} Wikipedia physics & chemistry articles...")
    data, titles = fetch_wikipedia_corpus(wiki_04_titles)
    sz = save_and_register_dataset(
        domain_id="04_physics_and_chemistry",
        domain_name="Physics and Chemistry",
        subtopic_id="04_03",
        subtopic_slug="chemical_reactions",
        subtopic_name="Chemical Reactions",
        source_slug="wikimedia_foundation_foundational_physics_chemistry",
        filename="wikimedia_foundation_foundational_physics_and_chemistry_corpus.txt",
        content_bytes=data,
        candidate_title="Wikimedia Comprehensive Physics, Mechanics & Chemical Reactions Corpus",
        source_platform="Wikimedia Foundation",
        publisher="Wikipedia Contributors",
        source_url="https://en.wikipedia.org/wiki/Special:Export",
        download_url="https://en.wikipedia.org/w/api.php",
        license_type="CC BY-SA 4.0 / GFDL",
        format_type="txt",
        description=f"Curated full-text revision corpus spanning {len(titles)} comprehensive encyclopedic articles on classical mechanics, Maxwellian electromagnetism, chemical thermodynamics, kinetics, and materials physics."
    )
    total_bytes += sz
    print(f"    Saved Physics & Chem Wikipedia Corpus: {sz / (1024*1024):.2f} MB ({len(titles)} articles)")

    # -------------------------------------------------------------------------
    # DOMAIN 05: SPACE AND THE UNIVERSE
    # -------------------------------------------------------------------------
    print("\n>>> Expanding 05_space_and_the_universe...")

    # 05_01: Camille Flammarion Popular Astronomy (pg60124)
    try:
        print("  - Downloading Camille Flammarion: Popular Astronomy...")
        data = download_direct_file("https://www.gutenberg.org/cache/epub/60124/pg60124.txt")
        sz = save_and_register_dataset(
            domain_id="05_space_and_the_universe",
            domain_name="Space and the Universe",
            subtopic_id="05_01",
            subtopic_slug="planets_and_the_solar_system",
            subtopic_name="Planets & the Solar System",
            source_slug="project_gutenberg_camille_flammarion_popular_astronomy",
            filename="camille_flammarion_popular_astronomy_complete.txt",
            content_bytes=data,
            candidate_title="Popular Astronomy: A General Description of the Heavens",
            source_platform="Project Gutenberg",
            publisher="Camille Flammarion (Project Gutenberg Release)",
            source_url="https://www.gutenberg.org/ebooks/60124",
            download_url="https://www.gutenberg.org/cache/epub/60124/pg60124.txt",
            license_type="Public Domain",
            format_type="txt",
            description="Comprehensive unabridged treatise by French astronomer Camille Flammarion detailing planetary physics, lunar geology, orbital dynamics, and stellar astrophysics."
        )
        total_bytes += sz
        print(f"    Saved Flammarion Astronomy: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Flammarion download failed: {e}")

    # 05_02: Robert Stawell Ball The Story of the Heavens (pg50285)
    try:
        print("  - Downloading Robert Stawell Ball: The Story of the Heavens...")
        data = download_direct_file("https://www.gutenberg.org/cache/epub/50285/pg50285.txt")
        sz = save_and_register_dataset(
            domain_id="05_space_and_the_universe",
            domain_name="Space and the Universe",
            subtopic_id="05_02",
            subtopic_slug="stars_and_galaxies",
            subtopic_name="Stars & Galaxies",
            source_slug="project_gutenberg_robert_ball_story_of_the_heavens",
            filename="robert_ball_story_of_the_heavens_complete.txt",
            content_bytes=data,
            candidate_title="The Story of the Heavens: Classical Astronomy and Astrophysics",
            source_platform="Project Gutenberg",
            publisher="Sir Robert Stawell Ball (Project Gutenberg Release)",
            source_url="https://www.gutenberg.org/ebooks/50285",
            download_url="https://www.gutenberg.org/cache/epub/50285/pg50285.txt",
            license_type="Public Domain",
            format_type="txt",
            description="Authoritative Victorian astrophysical treatise on variable stars, nebular hypotheses, cometary orbits, spectroscopic analysis of starlight, and double star systems."
        )
        total_bytes += sz
        print(f"    Saved Robert Ball Astronomy: {sz / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"    [ERROR] Robert Ball download failed: {e}")

    # 05 Wikipedia Deep Corpus
    wiki_05_titles = [
        "Solar_System", "Sun", "Mercury_(planet)", "Venus", "Earth", "Mars", "Jupiter",
        "Saturn", "Uranus", "Neptune", "Pluto", "Kuiper_belt", "Oort_cloud", "Asteroid_belt",
        "Moon", "Terrestrial_planet", "Gas_giant", "Planetary_ring", "Exoplanet", "Heliopause",
        "Star", "Galaxy", "Milky_Way", "Stellar_evolution", "Main_sequence", "Red_giant",
        "White_dwarf", "Neutron_star", "Supernova", "Pulsar", "Binary_star", "Star_cluster",
        "Globular_cluster", "Interstellar_medium", "Andromeda_Galaxy", "Nebula", "Planetary_nebula",
        "Quasar", "Active_galactic_nucleus", "Hertzsprung–Russell_diagram", "Space_exploration",
        "Timeline_of_spaceflight", "Apollo_program", "NASA", "European_Space_Agency",
        "Hubble_Space_Telescope", "James_Webb_Space_Telescope", "International_Space_Station",
        "Mars_rover", "Voyager_program", "Sputnik_1", "Moon_landing", "Artemis_program",
        "Space_Shuttle", "Orbit", "Rocket", "Escape_velocity", "Extravehicular_activity",
        "Satellite", "Black_hole", "Event_horizon", "Gravitational_singularity", "Hawking_radiation",
        "Gravitational_wave", "Supermassive_black_hole", "Cosmic_ray", "Gamma-ray_burst",
        "Big_Bang", "Cosmic_microwave_background", "Dark_matter", "Dark_energy",
        "Expansion_of_the_universe", "Physical_cosmology", "Spacetime", "Wormhole"
    ]
    print(f"  - Fetching {len(wiki_05_titles)} Wikipedia astronomy & cosmology articles...")
    data, titles = fetch_wikipedia_corpus(wiki_05_titles)
    sz = save_and_register_dataset(
        domain_id="05_space_and_the_universe",
        domain_name="Space and the Universe",
        subtopic_id="05_04",
        subtopic_slug="black_holes_and_cosmic_phenomena",
        subtopic_name="Black Holes & Cosmic Phenomena",
        source_slug="wikimedia_foundation_astrophysics_and_cosmology",
        filename="wikimedia_foundation_astrophysics_and_cosmology_corpus.txt",
        content_bytes=data,
        candidate_title="Wikimedia Comprehensive Solar System, Astrophysics & Cosmology Corpus",
        source_platform="Wikimedia Foundation",
        publisher="Wikipedia Contributors",
        source_url="https://en.wikipedia.org/wiki/Special:Export",
        download_url="https://en.wikipedia.org/w/api.php",
        license_type="CC BY-SA 4.0 / GFDL",
        format_type="txt",
        description=f"Curated full-text revision corpus spanning {len(titles)} comprehensive encyclopedic articles on comparative planetology, stellar astrophysics, gravitational wave cosmology, and space missions."
    )
    total_bytes += sz
    print(f"    Saved Space Wikipedia Corpus: {sz / (1024*1024):.2f} MB ({len(titles)} articles)")

    dt = time.time() - t0
    print("\n" + "=" * 70)
    print(f"CATEGORY A EXPANSION COMPLETED!")
    print(f"Total Bytes Downloaded: {total_bytes:,} bytes ({total_bytes / (1024*1024):.2f} MB)")
    print(f"Total Elapsed Time: {dt:.2f} seconds ({total_bytes / (1024*1024*dt):.2f} MB/s)")
    print("=" * 70)

if __name__ == "__main__":
    run_category_a()
