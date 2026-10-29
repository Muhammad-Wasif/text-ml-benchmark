# generate_full_catalog.py
# Generates the complete verified 200-subtopic catalog for all 50 domains

import json

categories = {
    "A": "Category A — Education, knowledge, and science",
    "B": "Category B — Nature, environment, and agriculture",
    "C": "Category C — Household and everyday life",
    "D": "Category D — Health, fitness, and personal development",
    "E": "Category E — Entertainment and media",
    "F": "Category F — Sports, hobbies, and recreation",
    "G": "Category G — Business, economy, and commerce",
    "H": "Category H — Technology and digital life",
    "I": "Category I — Society, public services, and infrastructure",
    "J": "Category J — Travel, communication, and human behavior"
}

# Define all 50 domains and their 4 subtopics with verified sources across platforms
RAW_DOMAINS = [
    # Domain 1
    ("01_education_and_studying", "Education and studying", "A", [
        ("01_01", "Study techniques and learning strategies", "Effective Study Strategies & Learning Techniques Knowledge Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Study_skills",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Study_skills|Active_recall|Spaced_repetition|Pomodoro_Technique&format=json",
         "CC-BY-SA 4.0", "en", "json", "study_skills_and_strategies.json", ["title", "extract"], ["Encyclopedia synthesis", "Requires standard CC-BY-SA attribution"]),
        ("01_02", "Exam preparation and revision", "MMLU High School Examination & Revision Benchmark",
         "Hugging Face", "https://huggingface.co/datasets/cais/mmlu",
         "https://datasets-server.huggingface.co/rows?dataset=cais%2Fmmlu&config=college_biology&split=test&offset=0&limit=100",
         "MIT", "en", "json", "mmlu_college_biology_revision.json", ["question", "choices", "answer"], ["Multiple-choice examination format", "Restricted to biology slice"]),
        ("01_03", "Student time management", "Student Time Management and Academic Productivity Reference Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Time_management",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Time_management|Procrastination|Time_blocking|Work%E2%80%93life_balance&format=json",
         "CC-BY-SA 4.0", "en", "json", "student_time_management_extracts.json", ["title", "extract"], ["Descriptive academic principles", "Qualitative conceptual text"]),
        ("01_04", "Academic performance and study habits", "Student Study Habits and Academic Performance Survey Dataset",
         "GitHub", "https://github.com/f111242256-dotcom/student-performance.csv-dataset",
         "https://raw.githubusercontent.com/f111242256-dotcom/student-performance.csv-dataset/main/Student_Performance.csv",
         "MIT", "en", "csv", "student_study_habits_performance.csv", ["Extracurricular Activities", "Sleep Hours", "Sample Question Papers Practiced"], ["Survey sample representation", "Mixed tabular and textual features"])
    ]),

    # Domain 2
    ("02_general_knowledge", "General knowledge", "A", [
        ("02_01", "World geography", "World Geography Countries and Territories Gazeteer Corpus",
         "GitHub", "https://github.com/mledoze/countries",
         "https://raw.githubusercontent.com/mledoze/countries/master/countries.json",
         "ODbL 1.0", "en", "json", "world_geography_countries_gazetteer.json", ["name", "capital", "region", "subregion"], ["Structured geo-entity database", "Political status per UN norms"]),
        ("02_02", "Historical civilizations", "Ancient Historical Civilizations Knowledge Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Cradle_of_civilization",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Indus_Valley_Civilisation|Ancient_Egypt|Mesopotamia|Ancient_Greece|Maya_civilization&format=json",
         "CC-BY-SA 4.0", "en", "json", "historical_civilizations_corpus.json", ["title", "extract"], ["Historiographical consensus summaries", "Varying archeological chronologies"]),
        ("02_03", "Discoveries and inventions", "Major Scientific Discoveries and Technological Inventions Timeline Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Timeline_of_historic_inventions",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Printing_press|Steam_engine|Electricity|Transistor|Penicillin&format=json",
         "CC-BY-SA 4.0", "en", "json", "discoveries_and_inventions_corpus.json", ["title", "extract"], ["Curated technological timeline narratives", "English focus"]),
        ("02_04", "Everyday facts about the world", "TriviaQA General World Knowledge Benchmark Samples",
         "Hugging Face", "https://huggingface.co/datasets/mandarjoshi/trivia_qa",
         "https://datasets-server.huggingface.co/rows?dataset=mandarjoshi%2Ftrivia_qa&config=rc&split=train&offset=0&limit=100",
         "Apache-2.0", "en", "json", "trivia_general_facts.json", ["question", "answer", "search_results"], ["Question-answer format", "Verification requires external checking"])
    ]),

    # Domain 3
    ("03_mathematics", "Mathematics", "A", [
        ("03_01", "Arithmetic and percentages", "GSM8K Grade School Arithmetic Word Problems",
         "Hugging Face", "https://huggingface.co/datasets/openai/gsm8k",
         "https://raw.githubusercontent.com/openai/grade-school-math/master/grade_school_math/data/test.jsonl",
         "MIT", "en", "jsonl", "gsm8k_arithmetic_word_problems.jsonl", ["question", "answer"], ["Grade-school multistep reasoning problems"]),
        ("03_02", "Algebra and equations", "Hendrycks MATH Algebra High-Level Mathematical Problems",
         "Hugging Face", "https://huggingface.co/datasets/themanas021/MATH-Algebra",
         "https://datasets-server.huggingface.co/rows?dataset=themanas021%2FMATH-Algebra&config=default&split=train&offset=0&limit=100",
         "MIT", "en", "json", "math_algebra_equations.json", ["problem", "solution"], ["LaTeX formatted mathematical equations", "Advanced competitive algebra"]),
        ("03_03", "Geometry and measurements", "MMLU High School Geometry Problem Explanations",
         "Hugging Face", "https://huggingface.co/datasets/cais/mmlu",
         "https://datasets-server.huggingface.co/rows?dataset=cais%2Fmmlu&config=high_school_mathematics&split=test&offset=0&limit=100",
         "MIT", "en", "json", "mmlu_high_school_geometry_math.json", ["question", "choices", "answer"], ["Multiple choice geometry problems", "Abstract spatial terminology"]),
        ("03_04", "Statistics and probability", "MMLU High School Statistics & Probability Problems",
         "Hugging Face", "https://huggingface.co/datasets/cais/mmlu",
         "https://datasets-server.huggingface.co/rows?dataset=cais%2Fmmlu&config=high_school_statistics&split=test&offset=0&limit=100",
         "MIT", "en", "json", "mmlu_statistics_probability.json", ["question", "choices", "answer"], ["Formal statistical questions", "Requires inferential interpretation"])
    ]),

    # Domain 4
    ("04_physics_and_chemistry", "Physics and chemistry", "A", [
        ("04_01", "Motion, force, and energy", "Conceptual Physics: Classical Mechanics, Motion, and Energy Corpus",
         "Hugging Face", "https://huggingface.co/datasets/cais/mmlu",
         "https://datasets-server.huggingface.co/rows?dataset=cais%2Fmmlu&config=conceptual_physics&split=test&offset=0&limit=100",
         "MIT", "en", "json", "conceptual_physics_mechanics.json", ["question", "choices", "answer"], ["Multiple-choice physics scenarios", "Focus on qualitative principles"]),
        ("04_02", "Electricity and magnetism", "College Physics: Electromagnetism and Circuits Knowledge Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Electromagnetism",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Electromagnetism|Magnetic_field|Electric_charge|Maxwell%27s_equations|Electromagnetic_induction&format=json",
         "CC-BY-SA 4.0", "en", "json", "electricity_magnetism_corpus.json", ["title", "extract"], ["Technical physics prose", "Expository conceptual explanations"]),
        ("04_03", "Chemical reactions", "Chemical Reactions and Stoichiometric Thermodynamics Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Chemical_reaction",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Chemical_reaction|Stoichiometry|Combustion|Redox|Acid%E2%80%93base_reaction&format=json",
         "CC-BY-SA 4.0", "en", "json", "chemical_reactions_stoichiometry_corpus.json", ["title", "extract"], ["Reaction kinetics and thermodynamic equilibria descriptions"]),
        ("04_04", "Materials and their properties", "Materials Science and Solid State Properties Knowledge Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Materials_science",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Materials_science|Strength_of_materials|Semiconductor|Superconductivity|Polymer&format=json",
         "CC-BY-SA 4.0", "en", "json", "materials_science_properties.json", ["title", "extract"], ["Materials classification definitions and mechanical properties overview"])
    ]),

    # Domain 5
    ("05_space_and_the_universe", "Space and the universe", "A", [
        ("05_01", "Planets and the solar system", "Solar System Planets and Celestial Bodies Knowledge Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Solar_System",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Solar_System|Mars|Jupiter|Saturn|Exoplanet&format=json",
         "CC-BY-SA 4.0", "en", "json", "solar_system_planets_corpus.json", ["title", "extract"], ["Planetary science overview", "Physical parameters included"]),
        ("05_02", "Stars and galaxies", "Stellar Astrophysics and Galactic Evolution Knowledge Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Galaxy",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Galaxy|Milky_Way|Star|Supernova|Nebula&format=json",
         "CC-BY-SA 4.0", "en", "json", "stars_and_galaxies_corpus.json", ["title", "extract"], ["Astrophysical definitions and deep space structures"]),
        ("05_03", "Black holes and cosmic phenomena", "Black Holes and Relativistic Cosmic Phenomena Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Black_hole",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Black_hole|Gravitational_wave|Neutron_star|Gamma-ray_burst|Quasar&format=json",
         "CC-BY-SA 4.0", "en", "json", "black_holes_cosmic_phenomena.json", ["title", "extract"], ["Theoretical physics and observational astrophysics summaries"]),
        ("05_04", "Space exploration and astronomy", "MMLU College Astronomy Benchmark and Questions",
         "Hugging Face", "https://huggingface.co/datasets/cais/mmlu",
         "https://datasets-server.huggingface.co/rows?dataset=cais%2Fmmlu&config=astronomy&split=test&offset=0&limit=100",
         "MIT", "en", "json", "mmlu_astronomy_space_exploration.json", ["question", "choices", "answer"], ["Astronomy and space science evaluation"])
    ]),

    # Domain 6
    ("06_nature_and_ecosystems", "Nature and ecosystems", "B", [
        ("06_01", "Forests and natural habitats", "Forest Ecosystems and Terrestrial Habitats Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Forest_ecology",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Forest_ecology|Rainforest|Boreal_forest|Temperate_deciduous_forest|Old-growth_forest&format=json",
         "CC-BY-SA 4.0", "en", "json", "forest_ecosystems_corpus.json", ["title", "extract"], ["Ecological terminology and canopy layers descriptions"]),
        ("06_02", "Mountains and valleys", "Mountain Geomorphology and Alpine Valleys Knowledge Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Mountain",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Mountain|Valley|Alpine_climate|Glacial_landform|Plate_tectonics&format=json",
         "CC-BY-SA 4.0", "en", "json", "mountains_and_valleys_corpus.json", ["title", "extract"], ["Geological formation mechanisms and high-altitude biomes"]),
        ("06_03", "Rivers and lakes", "Limnology, Freshwater Rivers and Lakes Knowledge Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/River",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=River|Lake|Limnology|Riparian_zone|Wetland&format=json",
         "CC-BY-SA 4.0", "en", "json", "rivers_and_lakes_corpus.json", ["title", "extract"], ["Freshwater hydrology and riparian ecology"]),
        ("06_04", "Deserts and grasslands", "Arid Ecosystems: Deserts, Steppes, and Grasslands Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Desert",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Desert|Grassland|Savanna|Steppe|Desertification&format=json",
         "CC-BY-SA 4.0", "en", "json", "deserts_and_grasslands_corpus.json", ["title", "extract"], ["Arid climate dynamics and xerophytic vegetation"])
    ]),

    # Domain 7
    ("07_trees_and_plants", "Trees and plants", "B", [
        ("07_01", "Tree species and their uses", "Dendrology: Global Tree Species and Economic Uses Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Tree",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Tree|Oak|Pine|Teak|Eucalyptus&format=json",
         "CC-BY-SA 4.0", "en", "json", "tree_species_uses_corpus.json", ["title", "extract"], ["Botanical classification and timber/industrial applications"]),
        ("07_02", "Plant growth and reproduction", "Plant Physiology, Photosynthesis, and Reproduction Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Plant_physiology",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Plant_physiology|Photosynthesis|Pollination|Seed_dispersal|Germination&format=json",
         "CC-BY-SA 4.0", "en", "json", "plant_growth_reproduction_corpus.json", ["title", "extract"], ["Biochemical plant processes and developmental biology"]),
        ("07_03", "Gardening and plant care", "Horticultural Care, Composting, and Urban Gardening Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Gardening",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Gardening|Horticulture|Pruning|Compost|Companion_planting&format=json",
         "CC-BY-SA 4.0", "en", "json", "gardening_and_plant_care_corpus.json", ["title", "extract"], ["Practical horticultural practices and cultivation techniques"]),
        ("07_04", "Medicinal and useful plants", "Ethnobotanical Pharmacology and Medicinal Plants Knowledge Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Medicinal_plants",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Medicinal_plants|Herbal_medicine|Pharmacognosy|Aloe_vera|Ginkgo_biloba&format=json",
         "CC-BY-SA 4.0", "en", "json", "medicinal_plants_corpus.json", ["title", "extract"], ["Traditional pharmacognosy and botanical active compounds"])
    ]),

    # Domain 8
    ("08_animals_and_wildlife", "Animals and wildlife", "B", [
        ("08_01", "Mammals and behavior", "Mammalian Ethology, Social Structure, and Behavior Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Mammal",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Mammal|Animal_behaviour|Primate|Carnivora|Cetacea&format=json",
         "CC-BY-SA 4.0", "en", "json", "mammals_and_behavior_corpus.json", ["title", "extract"], ["Zoological classification and behavioral ethology"]),
        ("08_02", "Birds and migration", "Ornithology: Bird Species and Avian Migration Systems Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Bird_migration",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Bird_migration|Ornithology|Flyway|Avian_navigation|Songbird&format=json",
         "CC-BY-SA 4.0", "en", "json", "birds_and_migration_corpus.json", ["title", "extract"], ["Navigation mechanisms and seasonal migratory routes"]),
        ("08_03", "Marine animals", "Marine Biology, Pelagic and Coral Reef Animals Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Marine_biology",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Marine_biology|Coral_reef|Whale|Shark|Cephalopod&format=json",
         "CC-BY-SA 4.0", "en", "json", "marine_animals_corpus.json", ["title", "extract"], ["Oceanic fauna and deep sea biological adaptations"]),
        ("08_04", "Wildlife habitats and conservation", "Wildlife Conservation and Biodiversity Protection Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Conservation_biology",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Conservation_biology|Endangered_species|IUCN_Red_List|Habitat_fragmentation|Rewilding&format=json",
         "CC-BY-SA 4.0", "en", "json", "wildlife_conservation_corpus.json", ["title", "extract"], ["Conservation status methodologies and ecological restoration"])
    ]),

    # Domain 9
    ("09_agriculture_and_farming", "Agriculture and farming", "B", [
        ("09_01", "Crop cultivation", "Agronomy: Cereal and Legume Crop Cultivation Manual Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Agronomy",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Agronomy|Crop_rotation|Tillage|Wheat|Rice&format=json",
         "CC-BY-SA 4.0", "en", "json", "crop_cultivation_agronomy_corpus.json", ["title", "extract"], ["Agricultural field management and crop yield factors"]),
        ("09_02", "Soil fertility and management", "Soil Science: Pedology, Nutrient Cycling, and Fertility Management Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Soil_fertility",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Soil_fertility|Humus|Nitrogen_cycle|Fertilizer|Soil_organic_matter&format=json",
         "CC-BY-SA 4.0", "en", "json", "soil_fertility_management_corpus.json", ["title", "extract"], ["Chemical macronutrients (NPK) and pedological properties"]),
        ("09_03", "Irrigation and water management", "Agricultural Irrigation Systems and Water Conservation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Irrigation",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Irrigation|Drip_irrigation|Water_efficiency|Canal|Groundwater_recharge&format=json",
         "CC-BY-SA 4.0", "en", "json", "irrigation_water_management_corpus.json", ["title", "extract"], ["Hydrological distribution techniques in arid and temperate farming"]),
        ("09_04", "Harvesting and crop storage", "Post-Harvest Grain Storage and Silo Preservation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Post-harvest_losses",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Post-harvest_losses|Silo|Grain_drying|Food_storage|Refrigeration&format=json",
         "CC-BY-SA 4.0", "en", "json", "harvesting_crop_storage_corpus.json", ["title", "extract"], ["Spoilage prevention mechanisms and modern bulk grain storage"])
    ]),

    # Domain 10
    ("10_weather_and_climate", "Weather and climate", "B", [
        ("10_01", "Rainfall and seasonal patterns", "Meteorology: Monsoon Systems and Global Precipitation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Rain",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Rain|Monsoon|Precipitation|Water_cycle|Season&format=json",
         "CC-BY-SA 4.0", "en", "json", "rainfall_seasonal_patterns_corpus.json", ["title", "extract"], ["Synoptic meteorological dynamics and global moisture circulation"]),
        ("10_02", "Temperature and humidity", "Atmospheric Thermodynamics: Humidity and Temperature Norms Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Humidity",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Humidity|Relative_humidity|Dew_point|Atmospheric_temperature|Lapse_rate&format=json",
         "CC-BY-SA 4.0", "en", "json", "temperature_humidity_thermodynamics.json", ["title", "extract"], ["Psychrometric parameters and thermal stratification"]),
        ("10_03", "Storms and severe weather", "Severe Weather: Tropical Cyclones, Tornadoes, and Thunderstorms Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Tropical_cyclone",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Tropical_cyclone|Tornado|Thunderstorm|Blizzard|Supercell&format=json",
         "CC-BY-SA 4.0", "en", "json", "severe_weather_storms_corpus.json", ["title", "extract"], ["Mesoscale convective systems and extreme atmospheric events"]),
        ("10_04", "Climate patterns and their effects", "Climatology: Climate Change and Oscillations Knowledge Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Climate_change",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Climate_change|El_Ni%C3%B1o%E2%80%93Southern_Oscillation|Global_warming|Carbon_cycle|Sea_level_rise&format=json",
         "CC-BY-SA 4.0", "en", "json", "climate_patterns_effects_corpus.json", ["title", "extract"], ["Macro-climatological indices and historical environmental changes"])
    ]),

    # Domain 11
    ("11_household_management", "Household management", "C", [
        ("11_01", "Cleaning and organization", "Domestic Sanitation, Cleaning, and Household Organizing Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Cleaning",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Cleaning|Sanitation|Housekeeping|Decluttering|Detergent&format=json",
         "CC-BY-SA 4.0", "en", "json", "cleaning_and_organization_corpus.json", ["title", "extract"], ["Domestic hygiene principles and chemical surfactant actions"]),
        ("11_02", "Laundry and clothing care", "Textile Care, Garment Laundering, and Fabric Preservation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Laundry",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Laundry|Fabric_care_label|Stain|Dry_cleaning|Ironing&format=json",
         "CC-BY-SA 4.0", "en", "json", "laundry_clothing_care_corpus.json", ["title", "extract"], ["Garment care symbolics and fabric maintenance procedures"]),
        ("11_03", "Household maintenance", "Residential Infrastructure, Plumbing, and Home Maintenance Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Home_repair",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Home_repair|Plumbing|Electrical_wiring|HVAC|Weatherization&format=json",
         "CC-BY-SA 4.0", "en", "json", "household_maintenance_repair_corpus.json", ["title", "extract"], ["Preventive home upkeep and mechanical diagnostics"]),
        ("11_04", "Daily household routines", "Domestic Ergonomics and Daily Home Routines Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Homemaking",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Homemaking|Domestic_technology|Chore|Time_management|Work%E2%80%93family_conflict&format=json",
         "CC-BY-SA 4.0", "en", "json", "daily_household_routines_corpus.json", ["title", "extract"], ["Domestic time allocation and household chore workflows"])
    ]),

    # Domain 12
    ("12_cooking_and_food", "Cooking and food", "C", [
        ("12_01", "Recipes and cooking methods", "Culinary Techniques, Gastronomy, and Recipes Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Cooking",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Cooking|Baking|Roasting|Saut%C3%A9ing|Sous_vide&format=json",
         "CC-BY-SA 4.0", "en", "json", "recipes_cooking_methods_corpus.json", ["title", "extract"], ["Thermal food preparation and classical culinary techniques"]),
        ("12_02", "Ingredients and substitutions", "Food Ingredients, Seasonings, and Culinary Substitutions Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Ingredient",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Ingredient|Spice|Herb|Sugar_substitute|Flour&format=json",
         "CC-BY-SA 4.0", "en", "json", "ingredients_substitutions_corpus.json", ["title", "extract"], ["Flavor profiles, culinary baking substitutes, and spices"]),
        ("12_03", "Food storage and preservation", "Food Science: Shelf-Life, Canning, and Preservation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Food_preservation",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Food_preservation|Canning|Pickling|Pasteurization|Freeze_drying&format=json",
         "CC-BY-SA 4.0", "en", "json", "food_storage_preservation_corpus.json", ["title", "extract"], ["Microbiological stabilization and food safety storage guidelines"]),
        ("12_04", "Meal preparation and planning", "Meal Planning, Menu Design, and Nutritional Preparation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Meal_preparation",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Meal_preparation|Dietary_guidelines|Menu|Batch_cooking|Nutrient_density&format=json",
         "CC-BY-SA 4.0", "en", "json", "meal_prep_planning_corpus.json", ["title", "extract"], ["Menu logistics and dietary nutritional planning"])
    ]),

    # Domain 13
    ("13_personal_finance", "Personal finance", "C", [
        ("13_01", "Monthly budgeting", "Personal Finance: Household Budgeting Strategies Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Budget",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Budget|Personal_budget|Zero-based_budgeting|Cash_flow|Savings_rate&format=json",
         "CC-BY-SA 4.0", "en", "json", "monthly_budgeting_corpus.json", ["title", "extract"], ["Personal financial allocations and budget balancing principles"]),
        ("13_02", "Saving money", "Emergency Funds, Frugal Living, and Compound Savings Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Saving",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Saving|Compound_interest|Emergency_fund|Frugality|Financial_independence&format=json",
         "CC-BY-SA 4.0", "en", "json", "saving_money_finance_corpus.json", ["title", "extract"], ["Savings accumulation frameworks and interest compounding"]),
        ("13_03", "Managing everyday expenses", "Consumer Expense Management and Debt Mitigation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Expense",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Expense|Credit_card_debt|Debt_consolidation|Fixed_cost|Variable_cost&format=json",
         "CC-BY-SA 4.0", "en", "json", "everyday_expenses_management_corpus.json", ["title", "extract"], ["Recurring liability analysis and consumer debt mitigation"]),
        ("13_04", "Comparing costs and value", "Consumer Economics: Cost-Benefit Analysis and Unit Valuation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Cost%E2%80%93benefit_analysis",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Cost%E2%80%93benefit_analysis|Opportunity_cost|Value_for_money|Unit_price|Total_cost_of_ownership&format=json",
         "CC-BY-SA 4.0", "en", "json", "cost_value_comparison_corpus.json", ["title", "extract"], ["Valuation metrics and comparative consumer purchasing"])
    ]),

    # Domain 14
    ("14_shopping_and_consumer_products", "Shopping and consumer products", "C", [
        ("14_01", "Product features and specifications", "Product Design Specifications and Consumer Engineering Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Product_specification",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Product_specification|Bill_of_materials|Product_lifecycle|Quality_control|ISO_9000&format=json",
         "CC-BY-SA 4.0", "en", "json", "product_features_specifications_corpus.json", ["title", "extract"], ["Engineering parameters and industrial quality standards"]),
        ("14_02", "Price and quality comparisons", "Consumer Reports: Price-Quality Heuristics and Benchmarks Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Benchmarking",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Benchmarking|Comparative_advertising|Consumer_protection|Price_dispersion|Signaling_(economics)&format=json",
         "CC-BY-SA 4.0", "en", "json", "price_quality_comparisons_corpus.json", ["title", "extract"], ["Economic signaling and consumer testing heuristics"]),
        ("14_03", "Customer reviews and feedback", "Customer Feedback Sentiment and Product Evaluation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Customer_review",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Customer_review|Net_Promoter|Customer_satisfaction|Word_of_mouth|Sentiment_analysis&format=json",
         "CC-BY-SA 4.0", "en", "json", "customer_reviews_feedback_corpus.json", ["title", "extract"], ["Consumer sentiment metrics and qualitative feedback loops"]),
        ("14_04", "Warranties and returns", "Consumer Rights: Warranty Law, Guarantees, and Return Policies Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Warranty",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Warranty|Extended_warranty|Product_liability|Cooling-off_period|Consumer_rights&format=json",
         "CC-BY-SA 4.0", "en", "json", "warranties_and_returns_corpus.json", ["title", "extract"], ["Statutory warranty regulations and return merchandise rights"])
    ]),

    # Domain 15
    ("15_daily_routines_and_productivity", "Daily routines and productivity", "C", [
        ("15_01", "Morning and evening routines", "Circadian Synchronization and Daily Habit Rituals Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Circadian_rhythm",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Circadian_rhythm|Sleep_hygiene|Chronotype|Morning_routine|Habit&format=json",
         "CC-BY-SA 4.0", "en", "json", "morning_evening_routines_corpus.json", ["title", "extract"], ["Sleep hygiene science and biological synchronization"]),
        ("15_02", "Task prioritization", "Productivity Systems: Prioritization and Deep Work Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Getting_Things_Done",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Getting_Things_Done|Eisenhower_method|Action_item|Deep_work|Task_management&format=json",
         "CC-BY-SA 4.0", "en", "json", "task_prioritization_productivity_corpus.json", ["title", "extract"], ["Action-oriented productivity frameworks"]),
        ("15_03", "Habit formation", "Behavioral Psychology: Habit Loops and Automaticity Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Habit",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Habit|Operant_conditioning|Reinforcement|Behavioural_change_theories|Self-control&format=json",
         "CC-BY-SA 4.0", "en", "json", "habit_formation_psychology_corpus.json", ["title", "extract"], ["Psychological cue-routine-reward architecture"]),
        ("15_04", "Managing distractions", "Cognitive Focus, Attention Economics, and Distraction Management Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Distraction",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Distraction|Attention_management|Digital_detox|Continuous_partial_attention|Flow_(psychology)&format=json",
         "CC-BY-SA 4.0", "en", "json", "managing_distractions_focus_corpus.json", ["title", "extract"], ["Attentional allocation and stimulus control strategies"])
    ]),

    # Domain 16
    ("16_general_health_education", "General health education", "D", [
        ("16_01", "Common illnesses and symptoms", "Medical Symptomatology and Clinical Pathology Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Symptom",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Symptom|Influenza|Common_cold|Fever|Hypertension&format=json",
         "CC-BY-SA 4.0", "en", "json", "common_illnesses_symptoms_corpus.json", ["title", "extract"], ["Clinical presentations and diagnostic symptom profiles"]),
        ("16_02", "Preventive health practices", "Public Health: Preventive Medicine and Prophylaxis Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Preventive_healthcare",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Preventive_healthcare|Vaccination|Screening_(medicine)|Epidemiology|Health_promotion&format=json",
         "CC-BY-SA 4.0", "en", "json", "preventive_health_practices_corpus.json", ["title", "extract"], ["Primary and secondary prevention protocols"]),
        ("16_03", "Hygiene and infection prevention", "Infection Control, Antisepsis, and Hygiene Standards Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Hygiene",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Hygiene|Hand_washing|Antiseptic|Transmission_(medicine)|Sterilization_(microbiology)&format=json",
         "CC-BY-SA 4.0", "en", "json", "hygiene_infection_prevention_corpus.json", ["title", "extract"], ["Aseptic techniques and pathogen transmission barriers"]),
        ("16_04", "Basic medical terminology", "Medical Etymology, Anatomical Planes, and Clinical Terminology Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Medical_terminology",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Medical_terminology|List_of_medical_roots,_suffixes_and_prefixes|Anatomical_terms_of_location|Pathology|Physiology&format=json",
         "CC-BY-SA 4.0", "en", "json", "basic_medical_terminology_corpus.json", ["title", "extract"], ["Standardized Greco-Latin morphological roots"])
    ]),

    # Domain 17
    ("17_mental_health_and_wellbeing", "Mental health and wellbeing", "D", [
        ("17_01", "Stress management", "Physiological and Cognitive Stress Regulation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Stress_management",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Stress_management|Cortisol|Chronic_stress|General_adaptation_syndrome|Psychological_resilience&format=json",
         "CC-BY-SA 4.0", "en", "json", "stress_management_corpus.json", ["title", "extract"], ["Endocrine stress response and behavioral interventions"]),
        ("17_02", "Emotional awareness", "Affective Psychology, Emotion Theory, and Granularity Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Emotional_intelligence",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Emotional_intelligence|Emotion|Self-awareness|Mood_(psychology)|Affect_(psychology)&format=json",
         "CC-BY-SA 4.0", "en", "json", "emotional_awareness_corpus.json", ["title", "extract"], ["Theories of emotion and emotional appraisal"]),
        ("17_03", "Relaxation and mindfulness", "Mindfulness-Based Stress Reduction and Autogenic Relaxation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Mindfulness",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Mindfulness|Meditation|Progressive_muscle_relaxation|Autogenic_training|Breathing_exercise&format=json",
         "CC-BY-SA 4.0", "en", "json", "relaxation_mindfulness_corpus.json", ["title", "extract"], ["Contemplative neuroscience and autonomic down-regulation"]),
        ("17_04", "Healthy coping strategies", "Cognitive Behavioral Therapy (CBT) and Coping Mechanisms Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Coping",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Coping|Cognitive_behavioral_therapy|Defence_mechanism|Cognitive_restructuring|Problem-solving&format=json",
         "CC-BY-SA 4.0", "en", "json", "healthy_coping_strategies_corpus.json", ["title", "extract"], ["Adaptive cognitive restructuring and emotional regulation"])
    ]),

    # Domain 18
    ("18_fitness_and_exercise", "Fitness and exercise", "D", [
        ("18_01", "Cardiovascular exercise", "Cardiovascular Conditioning, VO2 Max, and Aerobic Physiology Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Aerobic_exercise",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Aerobic_exercise|High-intensity_interval_training|VO2_max|Endurance_training|Heart_rate&format=json",
         "CC-BY-SA 4.0", "en", "json", "cardiovascular_exercise_corpus.json", ["title", "extract"], ["Cardiorespiratory endurance and mitochondrial adaptation"]),
        ("18_02", "Strength and resistance training", "Resistance Training Mechanics and Neuromuscular Adaptation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Strength_training",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Strength_training|Isometric_exercise|Motor_unit|Compound_exercise|Calisthenics&format=json",
         "CC-BY-SA 4.0", "en", "json", "strength_resistance_training_corpus.json", ["title", "extract"], ["Neuromuscular recruitment and force production principles"]),
        ("18_03", "Flexibility and mobility", "Joint Mobility, Range of Motion, and Flexibility Conditioning Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Flexibility_(anatomy)",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Flexibility_(anatomy)|Stretching|Joint_stability|Range_of_motion|Proprioceptive_neuromuscular_facilitation&format=json",
         "CC-BY-SA 4.0", "en", "json", "flexibility_mobility_conditioning_corpus.json", ["title", "extract"], ["Myofascial elasticity and articular mobility mechanics"]),
        ("18_04", "Exercise routines and recovery", "Exercise Periodization, Active Recovery, and DOMS Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Delayed_onset_muscle_soreness",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Delayed_onset_muscle_soreness|Sports_periodization|Active_recovery|Overtraining|Supercompensation&format=json",
         "CC-BY-SA 4.0", "en", "json", "exercise_routines_recovery_corpus.json", ["title", "extract"], ["Post-exercise physiological recovery and programming"])
    ]),

    # Domain 19
    ("19_gym_and_bodybuilding", "Gym and bodybuilding", "D", [
        ("19_01", "Training splits and workout planning", "Bodybuilding Workout Splits (PPL, Upper-Lower) Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Split_routine",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Split_routine|Weight_training|Circuit_training|Volume_(weight_training)|One-repetition_maximum&format=json",
         "CC-BY-SA 4.0", "en", "json", "gym_workout_splits_corpus.json", ["title", "extract"], ["Hypertrophy training volume and muscle frequency"]),
        ("19_02", "Muscle groups and exercise selection", "Skeletal Muscular Anatomy and Biomechanical Exercise Selection Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Muscle_hypertrophy",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Muscle_hypertrophy|Quadriceps|Pectoralis_major|Latissimus_dorsi_muscle|Biceps&format=json",
         "CC-BY-SA 4.0", "en", "json", "muscle_groups_exercise_selection_corpus.json", ["title", "extract"], ["Anatomical origins, insertions, and resistance curves"]),
        ("19_03", "Progressive overload", "Mechanisms of Progressive Overload and Mechanical Tension Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Progressive_overload",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Progressive_overload|Hypertrophy|Muscle_fatigue|Sarcoplasmic_hypertrophy|Workload&format=json",
         "CC-BY-SA 4.0", "en", "json", "progressive_overload_mechanisms_corpus.json", ["title", "extract"], ["Hypertrophy stimulus variables and load progression"]),
        ("19_04", "Rest, recovery, and training consistency", "Athletic Sleep Architecture, Deloading, and Systemic Recovery Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Sleep_and_athletic_performance",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Sleep_and_athletic_performance|Growth_hormone|Overtraining_syndrome|Rest_period|Fatigue_(physiology)&format=json",
         "CC-BY-SA 4.0", "en", "json", "training_recovery_consistency_corpus.json", ["title", "extract"], ["Systemic recovery markers and athletic adherence"])
    ]),

    # Domain 20
    ("20_nutrition_and_diet", "Nutrition and diet", "D", [
        ("20_01", "Macronutrients and micronutrients", "Human Nutritional Biochemistry: Macronutrients and Micronutrients Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Nutrient",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Nutrient|Protein_(nutrient)|Carbohydrate|Dietary_fat|Vitamin&format=json",
         "CC-BY-SA 4.0", "en", "json", "macronutrients_micronutrients_biochemistry.json", ["title", "extract"], ["Metabolic bioenergetics and vitamin/mineral biological roles"]),
        ("20_02", "Balanced meal planning", "Evidence-Based Dietetics and Nutritional Balance Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Healthy_diet",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Healthy_diet|Mediterranean_diet|Glycemic_index|Caloric_restriction|Dietary_fiber&format=json",
         "CC-BY-SA 4.0", "en", "json", "balanced_diet_meal_planning_corpus.json", ["title", "extract"], ["Dietary patterns and chronic disease risk reduction"]),
        ("20_03", "Hydration", "Osmoregulation, Fluid Balance, and Electrolyte Hydration Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Water_intoxication",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Fluid_balance|Dehydration|Electrolyte|Hyponatremia|Osmoregulation&format=json",
         "CC-BY-SA 4.0", "en", "json", "hydration_electrolyte_balance_corpus.json", ["title", "extract"], ["Renal fluid handling and exercise hydration demands"]),
        ("20_04", "Food labels and nutritional values", "Food Labeling Regulations and Nutritional Profiling Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Nutrition_facts_label",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Nutrition_facts_label|Daily_Value|Serving_size|Food_energy|Ingredients_list&format=json",
         "CC-BY-SA 4.0", "en", "json", "food_labels_nutritional_values_corpus.json", ["title", "extract"], ["Regulatory nutritional standards and disclosure frameworks"])
    ]),

    # Domain 21
    ("21_movies_and_cinema", "Movies and cinema", "E", [
        ("21_01", "Film genres and storytelling", "Cinema Studies: Narrative Structure, Film Genres, and Tropes Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Film_genre",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Film_genre|Film_noir|Science_fiction_film|Screenwriting|Three-act_structure&format=json",
         "CC-BY-SA 4.0", "en", "json", "film_genres_storytelling_corpus.json", ["title", "extract"], ["Cinematographic narrative conventions and taxonomy"]),
        ("21_02", "Movie reviews and ratings", "Film Criticism, Review Aggregation, and Rotten Tomatoes Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Film_criticism",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Film_criticism|Rotten_Tomatoes|Metacritic|Review_aggregator|Audience_reception&format=json",
         "CC-BY-SA 4.0", "en", "json", "movie_reviews_ratings_corpus.json", ["title", "extract"], ["Aesthetic evaluation methodologies and consensus scoring"]),
        ("21_03", "Filmmaking and production", "Cinematography, Mise-en-scène, and Film Production Technology Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Filmmaking",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Filmmaking|Cinematography|Mise-en-sc%C3%A8ne|Film_editing|Sound_design&format=json",
         "CC-BY-SA 4.0", "en", "json", "filmmaking_production_technology_corpus.json", ["title", "extract"], ["Technical cinematography and audio-visual post-production"]),
        ("21_04", "Box-office performance and audience reception", "Film Industry Economics and Box Office Distribution Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Box_office",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Box_office|Film_budget|Theatrical_window|Blockbuster_(entertainment)|Box_Office_Mojo&format=json",
         "CC-BY-SA 4.0", "en", "json", "box_office_audience_reception_corpus.json", ["title", "extract"], ["Theatrical financial performance and commercial dynamics"])
    ]),

    # Domain 22
    ("22_television_series", "Television series", "E", [
        ("22_01", "Episode summaries", "Television Studies: Episodic Structure and Series Synopses Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Television_show",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Television_show|Episode|Pilot_(television)|Cliffhanger|Season_finale&format=json",
         "CC-BY-SA 4.0", "en", "json", "tv_episode_summaries_corpus.json", ["title", "extract"], ["Broadcast episodic frameworks and serial synopses"]),
        ("22_02", "Character development", "Television Dramatic Character Arcs and Archetypes Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Character_arc",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Character_arc|Antihero|Protagonist|Ensemble_cast|Foil_(literature)&format=json",
         "CC-BY-SA 4.0", "en", "json", "tv_character_development_corpus.json", ["title", "extract"], ["Narrative psychological development across multi-episode runs"]),
        ("22_03", "Season comparisons", "Television Serial Continuity, Showrunning, and Season Comparisons Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Showrunner",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Showrunner|Golden_Age_of_Television_(2000s%E2%80%93present)|Serial_(radio_and_television)|Syndication|Television_pilot&format=json",
         "CC-BY-SA 4.0", "en", "json", "tv_season_comparisons_corpus.json", ["title", "extract"], ["Comparative structural changes across multi-year runs"]),
        ("22_04", "Story structure and plot progression", "Television Dramaturgy: Serialized vs Procedural Story Architecture Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Narrative_structure",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Narrative_structure|Procedural_drama|Story_arc|Foreshadowing|Plot_device&format=json",
         "CC-BY-SA 4.0", "en", "json", "story_structure_plot_progression_corpus.json", ["title", "extract"], ["Episodic progression models and dramaturgical pacing"])
    ]),

    # Domain 23
    ("23_pakistani_dramas", "Pakistani dramas", "E", [
        ("23_01", "Drama summaries and themes", "Pakistani Television Drama Industry and Thematic Summaries Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Pakistani_dramas",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Pakistani_dramas|Humsafar|Zindagi_Gulzar_Hai|Parizaad|Dhoop_Kinare&format=json",
         "CC-BY-SA 4.0", "en", "json", "pakistani_drama_summaries_themes.json", ["title", "extract"], ["Thematic overviews of prominent Urdu serials and cultural impact"]),
        ("23_02", "Character relationships", "Interpersonal Relationships and Family Dynamics in Pakistani Serials Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Hum_TV",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Hum_TV|ARY_Digital|Geo_Entertainment|Dastaan_(TV_series)|Alpha_Bravo_Charlie&format=json",
         "CC-BY-SA 4.0", "en", "json", "pakistani_drama_character_relationships.json", ["title", "extract"], ["Relational conflicts and social dramatization profiles"]),
        ("23_03", "Acting and direction reviews", "Pakistani Television Directorial Styles and Critical Accolades Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Lux_Style_Awards",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Lux_Style_Awards|Hum_Awards|Sultana_Siddiqui|Nadeem_Baig_(director)|Umera_Ahmad&format=json",
         "CC-BY-SA 4.0", "en", "json", "pakistani_drama_acting_direction_reviews.json", ["title", "extract"], ["Critical reception of scripts, direction, and awards"]),
        ("23_04", "Audience ratings and reception", "Broadcast Viewership, TRPs, and Digital Reach of Pakistani Dramas Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Television_in_Pakistan",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Television_in_Pakistan|Target_rating_point|Pakistan_Electronic_Media_Regulatory_Authority|Urdu_1|A-Plus_TV&format=json",
         "CC-BY-SA 4.0", "en", "json", "pakistani_drama_audience_ratings.json", ["title", "extract"], ["Rating methodologies and digital diaspora viewership trends"])
    ]),

    # Domain 24
    ("24_online_streaming_platforms", "Online streaming platforms", "E", [
        ("24_01", "Subscription plans and features", "Streaming Video On Demand (SVOD) Tiers and Platform Architecture Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Streaming_media",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Streaming_media|Subscription_business_model|Over-the-top_media_service|Video_on_demand|Digital_rights_management&format=json",
         "CC-BY-SA 4.0", "en", "json", "streaming_subscription_plans_features.json", ["title", "extract"], ["Commercial monetization structures and digital distribution tiers"]),
        ("24_02", "Content discovery and recommendations", "Recommender Systems and Algorithmic Discovery in Streaming Platforms Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Recommender_system",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Recommender_system|Collaborative_filtering|Content-based_filtering|Cold_start_(computing)|Netflix_Prize&format=json",
         "CC-BY-SA 4.0", "en", "json", "streaming_content_discovery_recommendations.json", ["title", "extract"], ["Algorithmic curation and user personalization mechanics"]),
        ("24_03", "Viewing habits", "Consumer Binge-Watching and Digital Media Consumption Patterns Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Binge-watching",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Binge-watching|Audience_measurement|Customer_attrition|Cord-cutting|Attention_span&format=json",
         "CC-BY-SA 4.0", "en", "json", "streaming_viewing_habits_corpus.json", ["title", "extract"], ["Behavioral consumption metrics and media psychological effects"]),
        ("24_04", "Platform usability and customer feedback", "Streaming Interface Usability, Buffering Latency, and UX Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Quality_of_experience",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Quality_of_experience|Adaptive_bitrate_streaming|Buffering_(telecommunication)|Usability|User_experience&format=json",
         "CC-BY-SA 4.0", "en", "json", "streaming_platform_usability_feedback.json", ["title", "extract"], ["Network buffering diagnostics and consumer UX criteria"])
    ]),

    # Domain 25
    ("25_books_and_literature", "Books and literature", "E", [
        ("25_01", "Fiction genres", "Literary Theory: Major Literary and Fiction Genres Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Literary_genre",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Literary_genre|Historical_fiction|Science_fiction|Gothic_fiction|Magical_realism&format=json",
         "CC-BY-SA 4.0", "en", "json", "literary_fiction_genres_corpus.json", ["title", "extract"], ["Taxonomic definitions of fictional styles and narrative conventions"]),
        ("25_02", "Book summaries and reviews", "Project Gutenberg Classic Literature Corpus Extracts",
         "Project Gutenberg", "https://www.gutenberg.org/",
         "https://www.gutenberg.org/cache/epub/11/pg11.txt",
         "Public Domain", "en", "txt", "alice_in_wonderland_gutenberg.txt", ["text"], ["Full unencumbered classic literary text"]),
        ("25_03", "Authors and literary styles", "Comparative Stylistics: Prose Voice and Authorial Techniques Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Style_(fiction)",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Style_(fiction)|Stream_of_consciousness|Point_of_view_(literature)|Tone_(literature)|Voice_(writing)&format=json",
         "CC-BY-SA 4.0", "en", "json", "authors_literary_styles_corpus.json", ["title", "extract"], ["Syntactic and stylistic narrative techniques"]),
        ("25_04", "Themes, symbolism, and character analysis", "Literary Analysis: Motifs, Symbolism, and Archetypes Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Theme_(literature)",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Theme_(literature)|Motif_(narrative)|Symbolism_(arts)|Archetype|Protagonist&format=json",
         "CC-BY-SA 4.0", "en", "json", "literary_themes_symbolism_corpus.json", ["title", "extract"], ["Hermeneutic analysis frameworks and symbolic interpretation"])
    ]),

    # Domain 26
    ("26_cricket", "Cricket", "F", [
        ("26_01", "Rules and match formats", "Laws of Cricket, Test, ODI, and T20 Format Regulations Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Laws_of_Cricket",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Laws_of_Cricket|Test_cricket|One_Day_International|Twenty20|Decision_Review_System&format=json",
         "CC-BY-SA 4.0", "en", "json", "cricket_rules_formats_corpus.json", ["title", "extract"], ["MCC official regulations and DRS adjudications"]),
        ("26_02", "Player statistics", "Cricket Analytics: Batting Averages, Economy, and Strike Rates Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Cricket_statistics",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Cricket_statistics|Batting_average|Bowling_average|Economy_rate|Strike_rate&format=json",
         "CC-BY-SA 4.0", "en", "json", "cricket_player_statistics_corpus.json", ["title", "extract"], ["Statistical metrics of player performance"]),
        ("26_03", "Match summaries", "Historic Cricket Match Summaries and Commentary Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/History_of_cricket",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=History_of_cricket|The_Ashes|Cricket_World_Cup|1992_Cricket_World_Cup|2019_Cricket_World_Cup&format=json",
         "CC-BY-SA 4.0", "en", "json", "cricket_match_summaries_corpus.json", ["title", "extract"], ["Innings recaps and tournament milestones"]),
        ("26_04", "Batting and bowling strategies", "Tactical Cricket: Swing, Spin Variations, and Field Placements Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Bowling_(cricket)",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Bowling_(cricket)|Batting_(cricket)|Swing_bowling|Spin_bowling|Fielding_(cricket)&format=json",
         "CC-BY-SA 4.0", "en", "json", "cricket_batting_bowling_strategies.json", ["title", "extract"], ["Technical aerodynamics of swing and tactical captaincy setups"])
    ]),

    # Domain 27
    ("27_football", "Football", "F", [
        ("27_01", "Rules and competitions", "IFAB Laws of the Game and International Football Competitions Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Laws_of_the_Game_(association_football)",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Laws_of_the_Game_(association_football)|FIFA_World_Cup|UEFA_Champions_League|Offside_(association_football)|Video_assistant_referee&format=json",
         "CC-BY-SA 4.0", "en", "json", "football_rules_competitions_corpus.json", ["title", "extract"], ["Official IFAB codified rules and tournament structures"]),
        ("27_02", "Player and team statistics", "Association Football Analytics: Expected Goals (xG) and Metrics Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Association_football_tactics_and_skills",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Association_football_tactics_and_skills|Clean_sheet|Assist_(association_football)|Cap_(sport)|Premier_League&format=json",
         "CC-BY-SA 4.0", "en", "json", "football_player_team_statistics.json", ["title", "extract"], ["Performance indices and tracking data"]),
        ("27_03", "Match reports", "Classic International Football Match Reports and Chronicles Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Miracle_of_Bern",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Miracle_of_Bern|2014_FIFA_World_Cup_semi-final|1966_FIFA_World_Cup_final|2022_FIFA_World_Cup_final|Maracanazo&format=json",
         "CC-BY-SA 4.0", "en", "json", "football_match_reports_corpus.json", ["title", "extract"], ["Detailed journalistic chronicles of historic finals"]),
        ("27_04", "Formations and tactics", "Tactical Football Theory: Gegenpressing, Tiki-Taka, and 4-3-3 Systems Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Formation_(association_football)",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Formation_(association_football)|Total_Football|Tiki-taka|Counter-attack|Zonal_marking&format=json",
         "CC-BY-SA 4.0", "en", "json", "football_formations_tactics_corpus.json", ["title", "extract"], ["Spatial pitch control, defensive pressing, and transition play"])
    ]),

    # Domain 28
    ("28_other_sports", "Other sports", "F", [
        ("28_01", "Badminton and tennis", "Racquet Sports: Tennis and Badminton Technical Play Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Tennis",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Tennis|Badminton|Grand_Slam_(tennis)|Serve_(tennis)|Smash_(tennis)&format=json",
         "CC-BY-SA 4.0", "en", "json", "badminton_tennis_racquet_sports.json", ["title", "extract"], ["Court geometry, stroke biomechanics, and rules"]),
        ("28_02", "Hockey and basketball", "Invasion Sports: Basketball Offense and Ice/Field Hockey Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Basketball",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Basketball|Ice_hockey|Field_hockey|Pick_and_roll|Fast_break&format=json",
         "CC-BY-SA 4.0", "en", "json", "hockey_basketball_sports_corpus.json", ["title", "extract"], ["Tactical set pieces and transition offensive execution"]),
        ("28_03", "Athletics and running", "Track and Field: Sprinting Biomechanics, Distance Running, and Decathlon Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Sport_of_athletics",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Sport_of_athletics|Sprint_(running)|Marathon|Decathlon|Long_jump&format=json",
         "CC-BY-SA 4.0", "en", "json", "athletics_and_running_corpus.json", ["title", "extract"], ["Locomotor biomechanics and physiological pacing"]),
        ("28_04", "Swimming and martial arts", "Aquatics and Combat Disciplines: Swimming Strokes and Martial Arts Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Swimming_(sport)",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Swimming_(sport)|Freestyle_swimming|Martial_arts|Judo|Taekwondo&format=json",
         "CC-BY-SA 4.0", "en", "json", "swimming_martial_arts_corpus.json", ["title", "extract"], ["Hydrodynamic propulsion and martial combat principles"])
    ]),

    # Domain 29
    ("29_gaming_and_esports", "Gaming and esports", "F", [
        ("29_01", "Game genres and mechanics", "Ludology: Game Design Mechanics, Core Loops, and Genres Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Game_mechanics",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Game_mechanics|Video_game_genre|Role-playing_video_game|First-person_shooter|Roguelike&format=json",
         "CC-BY-SA 4.0", "en", "json", "game_genres_mechanics_corpus.json", ["title", "extract"], ["Game loop architecture and emergent interactive design"]),
        ("29_02", "Player strategies and tactics", "Competitive Video Gaming: Meta-Strategies, Positioning, and Builds Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Multiplayer_online_battle_arena",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Multiplayer_online_battle_arena|Real-time_strategy|Speedrunning|Micro_(video_games)|Gamer&format=json",
         "CC-BY-SA 4.0", "en", "json", "gaming_strategies_tactics_corpus.json", ["title", "extract"], ["Tactical resource allocation and cooperative execution"]),
        ("29_03", "Game reviews", "Video Game Journalism, Ludic Evaluation, and Critical Reviews Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Video_game_journalism",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Video_game_journalism|The_Game_Awards|Game_criticism|Gameplay|Review_bombing&format=json",
         "CC-BY-SA 4.0", "en", "json", "video_game_reviews_journalism_corpus.json", ["title", "extract"], ["Evaluation of interactive ludonarrative harmony"]),
        ("29_04", "Esports performance and statistics", "Professional Esports Tournaments, Prize Pools, and Player Metrics Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Esports",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Esports|The_International_(Dota_2)|League_of_Legends_World_Championship|Major_Championship_(Counter-Strike)|Evolution_Championship_Series&format=json",
         "CC-BY-SA 4.0", "en", "json", "esports_performance_statistics_corpus.json", ["title", "extract"], ["Championship records and competitive tournament formats"])
    ]),

    # Domain 30
    ("30_hobbies_and_creative_activities", "Hobbies and creative activities", "F", [
        ("30_01", "Drawing and painting", "Visual Arts Theory: Painting Techniques, Media, and Chiaroscuro Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Painting",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Painting|Drawing|Color_theory|Chiaroscuro|Oil_painting&format=json",
         "CC-BY-SA 4.0", "en", "json", "drawing_and_painting_corpus.json", ["title", "extract"], ["Color harmonies and pigment composition mechanics"]),
        ("30_02", "Photography as a hobby, using text only", "Text-Based Photographic Theory: Exposure Triangle, Composition, and Optics Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Photography",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Photography|Aperture|Shutter_speed|Film_speed|Rule_of_thirds&format=json",
         "CC-BY-SA 4.0", "en", "json", "photography_theory_text_corpus.json", ["title", "extract"], ["Strict text-based exposure mechanics and framing"]),
        ("30_03", "Gardening and DIY crafts", "DIY Crafting, Joinery, and Domestic Handicrafts Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Do_it_yourself",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Do_it_yourself|Woodworking|Handicraft|Pottery|Upcycling&format=json",
         "CC-BY-SA 4.0", "en", "json", "diy_crafts_woodworking_corpus.json", ["title", "extract"], ["Manual fabrication techniques and tool handling"]),
        ("30_04", "Music theory and instrument learning, using text only", "Text-Based Musicology: Scales, Harmony, and Instrument Architecture Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Music_theory",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Music_theory|Scale_(music)|Chord_(music)|Circle_of_fifths|Musical_notation&format=json",
         "CC-BY-SA 4.0", "en", "json", "music_theory_text_corpus.json", ["title", "extract"], ["Strict text-based harmonic structures and intervals"])
    ]),

    # Domain 31
    ("31_economics", "Economics", "G", [
        ("31_01", "Inflation and purchasing power", "Macroeconomics: Inflation, Consumer Price Index, and Purchasing Power Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Inflation",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Inflation|Consumer_price_index|Purchasing_power|Hyperinflation|Central_bank&format=json",
         "CC-BY-SA 4.0", "en", "json", "inflation_purchasing_power_corpus.json", ["title", "extract"], ["Monetary policy economics and price index formulation"]),
        ("31_02", "Supply and demand", "Microeconomic Equilibrium: Price Elasticity and Market Forces Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Supply_and_demand",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Supply_and_demand|Price_elasticity_of_demand|Economic_equilibrium|Deadweight_loss|Consumer_surplus&format=json",
         "CC-BY-SA 4.0", "en", "json", "supply_and_demand_microeconomics.json", ["title", "extract"], ["Market clearing dynamics and elasticity coefficients"]),
        ("31_03", "Employment and wages", "Labor Economics: Unemployment, Wage Determination, and Human Capital Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Labour_economics",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Labour_economics|Unemployment|Minimum_wage|Human_capital|Collective_bargaining&format=json",
         "CC-BY-SA 4.0", "en", "json", "employment_wages_labor_economics.json", ["title", "extract"], ["Labor market equilibrium and wage rigidity"]),
        ("31_04", "Production and economic growth", "Macroeconomic Growth Theory: GDP, Productivity, and Solow Models Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Economic_growth",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Economic_growth|Gross_domestic_product|Total_factor_productivity|Solow%E2%80%93Swan_model|Capital_accumulation&format=json",
         "CC-BY-SA 4.0", "en", "json", "production_economic_growth_corpus.json", ["title", "extract"], ["Production functions and technological capital deepening"])
    ]),

    # Domain 32
    ("32_e_commerce", "E-commerce", "G", [
        ("32_01", "Online ordering and checkout", "E-Commerce Architecture: Shopping Cart, Payment Gateways, and Checkout UX Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/E-commerce",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=E-commerce|Payment_gateway|Shopping_cart_software|Abandonment_rate|Online_shopping&format=json",
         "CC-BY-SA 4.0", "en", "json", "online_ordering_checkout_corpus.json", ["title", "extract"], ["Checkout funnel friction and payment encryption standards"]),
        ("32_02", "Product listings and descriptions", "Pakistan Biggest E-Commerce Real World Catalog Dataset",
         "Hugging Face", "https://huggingface.co/datasets/sajeelkazmi/PakistanBiggestEcommerceDatasetCleaned",
         "https://datasets-server.huggingface.co/rows?dataset=sajeelkazmi%2FPakistanBiggestEcommerceDatasetCleaned&config=default&split=train&offset=0&limit=100",
         "Apache-2.0", "en", "json", "ecommerce_pakistan_catalog.json", ["item_id", "category_name_1", "status", "price"], ["Real-world South Asian e-commerce retail transactions"]),
        ("32_03", "Shipping and delivery", "Logistics Engineering: Last-Mile Delivery, Fulfillment, and Tracking Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Last_mile_(transportation)",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Last_mile_(transportation)|Order_fulfillment|Supply_chain_management|Freight_forwarding|Package_tracking&format=json",
         "CC-BY-SA 4.0", "en", "json", "shipping_and_delivery_logistics_corpus.json", ["title", "extract"], ["Distribution network routing and courier logistics"]),
        ("32_04", "Returns, refunds, and customer support", "Reverse Logistics: RMA, Refund Policies, and Merchant Dispute Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Reverse_logistics",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Reverse_logistics|Return_merchandise_authorization|Customer_service|Chargeback|Help_desk&format=json",
         "CC-BY-SA 4.0", "en", "json", "returns_refunds_support_corpus.json", ["title", "extract"], ["Merchant return workflows and dispute adjudication"])
    ]),

    # Domain 33
    ("33_small_businesses_and_entrepreneurship", "Small businesses and entrepreneurship", "G", [
        ("33_01", "Business ideas and market research", "Entrepreneurship: Value Proposition, TAM/SAM/SOM, and Market Feasibility Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Entrepreneurship",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Entrepreneurship|Market_research|Business_model|Business_plan|Feasibility_study&format=json",
         "CC-BY-SA 4.0", "en", "json", "business_ideas_market_research_corpus.json", ["title", "extract"], ["Venture ideation and market sizing methodologies"]),
        ("33_02", "Startup costs and budgeting", "Venture Finance: Seed Capital, Burn Rate, and Startup Budgeting Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Startup_company",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Startup_company|Seed_money|Venture_capital|Burn_rate|Working_capital&format=json",
         "CC-BY-SA 4.0", "en", "json", "startup_costs_budgeting_corpus.json", ["title", "extract"], ["Financial runway management and initial capital expenditure"]),
        ("33_03", "Customer acquisition", "SMB Growth: Customer Acquisition Cost (CAC), Funnels, and Lead Generation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Customer_acquisition",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Customer_acquisition|Lead_generation|Purchase_funnel|Customer_lifetime_value|Inbound_marketing&format=json",
         "CC-BY-SA 4.0", "en", "json", "customer_acquisition_growth_corpus.json", ["title", "extract"], ["Acquisition metrics and conversion optimization"]),
        ("33_04", "Business operations and growth", "Small Business Operations: Standard Operating Procedures and Scaling Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Business_operations",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Business_operations|Standard_operating_procedure|Small_business|Economies_of_scale|Franchising&format=json",
         "CC-BY-SA 4.0", "en", "json", "business_operations_growth_corpus.json", ["title", "extract"], ["Operational efficiency and scaling milestones"])
    ]),

    # Domain 34
    ("34_marketing_and_advertising", "Marketing and advertising", "G", [
        ("34_01", "Brand positioning", "Strategic Marketing: Brand Equity, Positioning, and Archetypes Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Brand",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Brand|Positioning_(marketing)|Brand_equity|Unique_selling_proposition|Corporate_identity&format=json",
         "CC-BY-SA 4.0", "en", "json", "brand_positioning_marketing_corpus.json", ["title", "extract"], ["Perceptual mapping and competitive differentiation"]),
        ("34_02", "Advertising strategies", "Advertising Theory: Copywriting, AIDA Model, and Media Planning Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Advertising",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Advertising|Copywriting|AIDA_(marketing)|Media_planning|Advertising_campaign&format=json",
         "CC-BY-SA 4.0", "en", "json", "advertising_strategies_theory_corpus.json", ["title", "extract"], ["Persuasion models and multi-channel media buys"]),
        ("34_03", "Customer segmentation", "Market Segmentation: Demographics, Psychographics, and Behavioral Clusters Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Market_segmentation",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Market_segmentation|Target_audience|Persona_(user_experience)|Psychographics|Demographic_profile&format=json",
         "CC-BY-SA 4.0", "en", "json", "customer_segmentation_clusters_corpus.json", ["title", "extract"], ["Targeted persona construction and demographic stratification"]),
        ("34_04", "Campaign performance and engagement", "Marketing Analytics: CTR, ROAS, and Attribution Modeling Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Marketing_performance_measurement_and_management",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Marketing_performance_measurement_and_management|Click-through_rate|Conversion_rate|Attribution_(marketing)|Key_performance_indicator&format=json",
         "CC-BY-SA 4.0", "en", "json", "campaign_performance_engagement_corpus.json", ["title", "extract"], ["Digital engagement attribution and conversion analytics"])
    ]),

    # Domain 35
    ("35_jobs_and_careers", "Jobs and careers", "G", [
        ("35_01", "Job descriptions and requirements", "Occupational Competencies and Standard Job Descriptions Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Job_description",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Job_description|Profession|Occupation|Job_analysis|Recruitment&format=json",
         "CC-BY-SA 4.0", "en", "json", "job_descriptions_requirements_corpus.json", ["title", "extract"], ["Competency prerequisites and role classification"]),
        ("35_02", "Resume and interview preparation", "Career Development: Resume Crafting and Behavioral Interviewing Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/R%C3%A9sum%C3%A9",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=R%C3%A9sum%C3%A9|Job_interview|Curriculum_vitae|Cover_letter|Situation,_task,_action_and_result&format=json",
         "CC-BY-SA 4.0", "en", "json", "resume_interview_prep_corpus.json", ["title", "extract"], ["STAR interview methodology and resume structuring"]),
        ("35_03", "Career planning", "Organizational Psychology: Career Paths, Mentorship, and Trajectories Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Career_development",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Career_development|Mentorship|Promotion_(rank)|Skill_management|Continuing_education&format=json",
         "CC-BY-SA 4.0", "en", "json", "career_planning_development_corpus.json", ["title", "extract"], ["Career ladder progression and skill gap bridging"]),
        ("35_04", "Workplace skills and professional development", "Workplace Soft Skills, Leadership, and Professional Development Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Soft_skills",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Soft_skills|Communication|Leadership|Teamwork|Workplace_conflict&format=json",
         "CC-BY-SA 4.0", "en", "json", "workplace_skills_professional_development.json", ["title", "extract"], ["Executive presence, active listening, and conflict de-escalation"])
    ]),

    # Domain 36
    ("36_websites_and_web_services", "Websites and web services", "H", [
        ("36_01", "Website usability", "HCI Usability Engineering: Nielsen Norman Heuristics and User Flow Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Usability",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Usability|Heuristic_evaluation|User_interface_design|Usability_testing|Human%E2%80%93computer_interaction&format=json",
         "CC-BY-SA 4.0", "en", "json", "website_usability_heuristics_corpus.json", ["title", "extract"], ["Nielsen's 10 heuristics and cognitive walkthroughs"]),
        ("36_02", "Navigation and information structure", "Information Architecture: Taxonomies, Sitemaps, and Navigation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Information_architecture",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Information_architecture|Site_map|Breadcrumb_navigation|Faceted_search|Taxonomy_(general)&format=json",
         "CC-BY-SA 4.0", "en", "json", "information_architecture_navigation_corpus.json", ["title", "extract"], ["Ontological hierarchies and faceted navigation principles"]),
        ("36_03", "Accessibility and readability", "Web Accessibility: W3C WCAG Guidelines and Readability Standards Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Web_accessibility",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Web_accessibility|Web_Content_Accessibility_Guidelines|Screen_reader|Readability|Color_blindness&format=json",
         "CC-BY-SA 4.0", "en", "json", "web_accessibility_wcag_corpus.json", ["title", "extract"], ["WCAG 2.1 compliance criteria and assistive tech support"]),
        ("36_04", "Website performance descriptions and user feedback", "Web Performance Engineering: Core Web Vitals and Latency Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Web_performance",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Web_performance|PageSpeed_Insights|Content_delivery_network|Minification_(programming)|Browser_cache&format=json",
         "CC-BY-SA 4.0", "en", "json", "website_performance_vitals_corpus.json", ["title", "extract"], ["LCP, FID, CLS performance thresholds and caching"])
    ]),

    # Domain 37
    ("37_computers_and_operating_systems", "Computers and operating systems", "H", [
        ("37_01", "Hardware specifications", "Computer Architecture: Microprocessors, Memory Busses, and Storage Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Computer_hardware",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Computer_hardware|Central_processing_unit|Random-access_memory|Solid-state_drive|PCI_Express&format=json",
         "CC-BY-SA 4.0", "en", "json", "computer_hardware_specifications_corpus.json", ["title", "extract"], ["Microarchitecture bus widths, cache hierarchies, and protocols"]),
        ("37_02", "Operating system features", "Operating Systems Theory: Kernels, Virtual Memory, and Scheduling Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Operating_system",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Operating_system|Kernel_(operating_system)|Virtual_memory|Scheduling_(computing)|File_system&format=json",
         "CC-BY-SA 4.0", "en", "json", "operating_system_features_corpus.json", ["title", "extract"], ["Process scheduling algorithms and page fault handling"]),
        ("37_03", "Computer troubleshooting", "IT Systems Administration: Hardware Diagnostics and Error Remediation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Troubleshooting",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Troubleshooting|Blue_screen_of_death|Device_driver|Power-on_self-test|Firmware&format=json",
         "CC-BY-SA 4.0", "en", "json", "computer_troubleshooting_diagnostics_corpus.json", ["title", "extract"], ["POST codes, memory fault isolation, and driver recovery"]),
        ("37_04", "Device maintenance and upgrades", "PC Maintenance: Thermal Management, BIOS Flashing, and Upgrades Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Computer_cooling",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Computer_cooling|Thermal_paste|UEFI|Cable_management|Overclocking&format=json",
         "CC-BY-SA 4.0", "en", "json", "pc_maintenance_upgrades_corpus.json", ["title", "extract"], ["Thermal interface conduction and firmware maintenance"])
    ]),

    # Domain 38
    ("38_smartphones_and_mobile_apps", "Smartphones and mobile apps", "H", [
        ("38_01", "Phone specifications and comparisons", "Mobile Technology: Smartphone SoCs, Displays, and Sensors Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Smartphone",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Smartphone|System_on_a_chip|OLED|Camera_sensor|IP_code&format=json",
         "CC-BY-SA 4.0", "en", "json", "smartphone_specifications_comparisons_corpus.json", ["title", "extract"], ["Heterogeneous mobile silicon and display metrics"]),
        ("38_02", "App features and reviews", "Mobile Application Ecosystems: App Store Dynamics and Software Features Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Mobile_app",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Mobile_app|Google_Play|App_Store_(Apple)|In-app_purchase|Push_technology&format=json",
         "CC-BY-SA 4.0", "en", "json", "mobile_apps_features_reviews_corpus.json", ["title", "extract"], ["Application distribution frameworks and user rating mechanisms"]),
        ("38_03", "Battery life and device usage", "Mobile Energy Optimization: Lithium-Ion Degradation and Screen Time Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Lithium-ion_battery",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Lithium-ion_battery|Battery_management_system|Screen_time|Fast_charging|Power_management&format=json",
         "CC-BY-SA 4.0", "en", "json", "mobile_battery_usage_corpus.json", ["title", "extract"], ["Electrochemical cycle wear and OS background throttling"]),
        ("38_04", "Mobile usability and troubleshooting", "Mobile UX Guidelines, Touch Latency, and OS Troubleshooting Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Mobile_operating_system",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Mobile_operating_system|Android_(operating_system)|IOS|Touchscreen|Safe_mode&format=json",
         "CC-BY-SA 4.0", "en", "json", "mobile_usability_troubleshooting_corpus.json", ["title", "extract"], ["Gesture ergonomics and recovery partition workflows"])
    ]),

    # Domain 39
    ("39_internet_and_computer_networks", "Internet and computer networks", "H", [
        ("39_01", "Network terminology", "Telecommunications: OSI Model, TCP/IP Suite, and Routing Terminology Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Internet_protocol_suite",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Internet_protocol_suite|OSI_model|Domain_Name_System|IPv6|Subnetwork&format=json",
         "CC-BY-SA 4.0", "en", "json", "network_terminology_protocols_corpus.json", ["title", "extract"], ["Formal protocol layer models and packet headers"]),
        ("39_02", "Internet speed and connectivity", "Broadband Metrics: Throughput, Latency, Jitter, and Packet Loss Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Broadband",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Broadband|Latency_(engineering)|Jitter|Packet_loss|Bandwidth_(computing)&format=json",
         "CC-BY-SA 4.0", "en", "json", "internet_speed_connectivity_corpus.json", ["title", "extract"], ["Network transmission characteristics and bandwidth limits"]),
        ("39_03", "Wi-Fi troubleshooting", "Wireless Local Area Networks: 802.11 Protocols and Interference Mitigation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Wi-Fi",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Wi-Fi|IEEE_802.11|Electromagnetic_interference|Wireless_access_point|WPA3&format=json",
         "CC-BY-SA 4.0", "en", "json", "wifi_troubleshooting_corpus.json", ["title", "extract"], ["Radio frequency channel allocation and encryption"]),
        ("39_04", "Network reliability and performance", "Network Engineering: QoS, SLA Uptime, and Diagnostics Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Quality_of_service",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Quality_of_service|Traceroute|Ping_(networking_utility)|Service-level_agreement|High_availability&format=json",
         "CC-BY-SA 4.0", "en", "json", "network_reliability_performance_corpus.json", ["title", "extract"], ["Packet prioritization algorithms and network diagnostics"])
    ]),

    # Domain 40
    ("40_artificial_intelligence_and_data_science", "Artificial intelligence and data science", "H", [
        ("40_01", "Machine learning concepts", "Machine Learning Foundations: Supervised, Unsupervised, and Gradient Descent Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Machine_learning",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Machine_learning|Supervised_learning|Overfitting|Gradient_descent|Cross-validation_(statistics)&format=json",
         "CC-BY-SA 4.0", "en", "json", "machine_learning_concepts_corpus.json", ["title", "extract"], ["Statistical learning theory and optimization algorithms"]),
        ("40_02", "Data analysis and interpretation", "Exploratory Data Analysis: Distributions, p-Values, and Causality Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Data_analysis",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Data_analysis|Exploratory_data_analysis|Statistical_hypothesis_testing|P-value|Correlation_does_not_imply_causation&format=json",
         "CC-BY-SA 4.0", "en", "json", "data_analysis_interpretation_corpus.json", ["title", "extract"], ["Inferential statistics and observational study pitfalls"]),
        ("40_03", "AI applications in daily life", "Applied AI: Natural Language Processing, Vision, and Autonomous Systems Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Applications_of_artificial_intelligence",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Applications_of_artificial_intelligence|Natural_language_processing|Computer_vision|Speech_recognition|Autonomous_car&format=json",
         "CC-BY-SA 4.0", "en", "json", "ai_applications_daily_life_corpus.json", ["title", "extract"], ["Commercial deployments and interactive machine intelligence"]),
        ("40_04", "AI limitations, reliability, and evaluation", "AI Alignment, Bias, Hallucination, and Benchmark Evaluation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Hallucination_(artificial_intelligence)|Algorithmic_bias|AI_safety|Evaluation_measures_(information_retrieval)|Perplexity&format=json",
         "CC-BY-SA 4.0", "en", "json", "ai_limitations_reliability_corpus.json", ["title", "extract"], ["Model failure modes and formal evaluation metrics"])
    ]),

    # Domain 41
    ("41_population_and_demographics", "Population and demographics", "I", [
        ("41_01", "Population growth", "Demography: Global Population Trajectory and Demographic Transition Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Demography",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Demography|Demographic_transition|Total_fertility_rate|Mortality_rate|Overpopulation&format=json",
         "CC-BY-SA 4.0", "en", "json", "population_growth_demography_corpus.json", ["title", "extract"], ["Demographic transition model phases and vital statistics"]),
        ("41_02", "Age distribution", "Population Pyramids, Dependency Ratios, and Demographic Aging Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Population_pyramid",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Population_pyramid|Population_ageing|Dependency_ratio|Baby_boom|Median_age&format=json",
         "CC-BY-SA 4.0", "en", "json", "age_distribution_pyramids_corpus.json", ["title", "extract"], ["Age cohort distributions and macroeconomic dependency"]),
        ("41_03", "Urbanization and migration", "Human Geography: Urbanization, Megacities, and Rural-Urban Migration Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Urbanization",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Urbanization|Megacity|Human_migration|Rural-urban_fringe|Suburbanization&format=json",
         "CC-BY-SA 4.0", "en", "json", "urbanization_migration_geography_corpus.json", ["title", "extract"], ["Spatial demographic concentration and mobility"]),
        ("41_04", "Household size and composition", "Family Sociology: Household Composition, Single Living, and Family Structures Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Household",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Household|Nuclear_family|Extended_family|Single-person_household|Cohabitation&format=json",
         "CC-BY-SA 4.0", "en", "json", "household_size_composition_corpus.json", ["title", "extract"], ["Domestic structural evolution in industrial societies"])
    ]),

    # Domain 42
    ("42_transportation_and_traffic", "Transportation and traffic", "I", [
        ("42_01", "Traffic congestion", "Traffic Engineering: Bottleneck Phenomena, Congestion Pricing, and Flow Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Traffic_congestion",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Traffic_congestion|Traffic_flow|Congestion_pricing|Induced_demand|Gridlock&format=json",
         "CC-BY-SA 4.0", "en", "json", "traffic_congestion_engineering_corpus.json", ["title", "extract"], ["Hydrodynamic traffic flow models and pricing"]),
        ("42_02", "Road safety and driving behavior", "Vehicular Safety: Defensive Driving, Collision Analysis, and Restraints Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Road_traffic_safety",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Road_traffic_safety|Defensive_driving|Seat_belt|Speed_limit|Traffic_collision&format=json",
         "CC-BY-SA 4.0", "en", "json", "road_safety_driving_behavior_corpus.json", ["title", "extract"], ["Passive/active vehicular safety and collision statistics"]),
        ("42_03", "Public transport services", "Urban Transit Systems: BRT, Metro Rail, and Multimodal Transit Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Public_transport",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Public_transport|Bus_rapid_transit|Rapid_transit|Commuter_rail|Fare_evasion&format=json",
         "CC-BY-SA 4.0", "en", "json", "public_transport_services_corpus.json", ["title", "extract"], ["Mass transit scheduling and headway engineering"]),
        ("42_04", "Travel time and route planning", "Algorithmic Route Navigation, Commuting Time, and Isochrones Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Dijkstra%27s_algorithm|Route_assignment|Commuting|Isochrone_map|Turn-by-turn_navigation&format=json",
         "CC-BY-SA 4.0", "en", "json", "route_planning_navigation_corpus.json", ["title", "extract"], ["Graph traversal algorithms and travel impedance functions"])
    ]),

    # Domain 43
    ("43_emergencies_and_disaster_preparedness", "Emergencies and disaster preparedness", "I", [
        ("43_01", "Fire safety", "Fire Protection Engineering: Extinguishment, Alarms, and Evacuation Plans Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Fire_safety",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Fire_safety|Fire_extinguisher|Smoke_detector|Fire_door|Emergency_evacuation&format=json",
         "CC-BY-SA 4.0", "en", "json", "fire_safety_evacuation_corpus.json", ["title", "extract"], ["Combustion classes and life-safety egress standards"]),
        ("43_02", "Earthquake preparedness", "Seismological Safety: Seismic Retrofitting, Shaking Protocols, and Emergency Kits Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Earthquake_preparedness",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Earthquake_preparedness|Seismic_retrofit|Tsunami_warning_system|Earthquake_engineering|Liquefaction&format=json",
         "CC-BY-SA 4.0", "en", "json", "earthquake_preparedness_corpus.json", ["title", "extract"], ["Seismic wave mitigation and structural resilience"]),
        ("43_03", "Flood preparedness", "Hydrological Mitigation: Levees, Sump Pumps, and Flood Warning Systems Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Flood_control",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Flood_control|Levee|Flash_flood|Floodplain_management|Sandbag&format=json",
         "CC-BY-SA 4.0", "en", "json", "flood_preparedness_control_corpus.json", ["title", "extract"], ["Flood basin zoning and hydrological barriers"]),
        ("43_04", "Emergency response procedures", "Civil Protection: Incident Command System, Triage, and 72-Hour Kits Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Incident_Command_System",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Incident_Command_System|Emergency_management|Triage|Disaster_response|Survival_kit&format=json",
         "CC-BY-SA 4.0", "en", "json", "emergency_response_procedures_corpus.json", ["title", "extract"], ["Standardized emergency response hierarchies and resource management"])
    ]),

    # Domain 44
    ("44_water_and_sanitation", "Water and sanitation", "I", [
        ("44_01", "Drinking water quality", "Potable Water Engineering: WHO Standards, Contaminants, and Filtration Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Drinking_water_quality_standards",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Drinking_water_quality_standards|Water_purification|Turbidity|Chlorination|Reverse_osmosis&format=json",
         "CC-BY-SA 4.0", "en", "json", "drinking_water_quality_corpus.json", ["title", "extract"], ["Maximum contaminant levels (MCL) and disinfection chemistry"]),
        ("44_02", "Water conservation", "Resource Management: Xeriscaping, Low-Flow Fixtures, and Conservation Policies Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Water_conservation",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Water_conservation|Xeriscaping|Rainwater_harvesting|Greywater|Water_meter&format=json",
         "CC-BY-SA 4.0", "en", "json", "water_conservation_management_corpus.json", ["title", "extract"], ["Municipal demand reduction and fixture efficiency"]),
        ("44_03", "Wastewater and sewage management", "Environmental Engineering: Activated Sludge, Clarification, and Effluents Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Wastewater_treatment",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Wastewater_treatment|Activated_sludge|Septic_tank|Sewage|Biochemical_oxygen_demand&format=json",
         "CC-BY-SA 4.0", "en", "json", "wastewater_sewage_management_corpus.json", ["title", "extract"], ["Biological oxidation and anaerobic sludge digestion"]),
        ("44_04", "Household water consumption", "Residential Hydrology: End-Use Water Breakdown and Leak Detection Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Residential_water_use_in_the_US_and_Canada",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Residential_water_use_in_the_US_and_Canada|Water_footprint|Plumbing_fixture|Smart_water_metering|Water_scarcity&format=json",
         "CC-BY-SA 4.0", "en", "json", "household_water_consumption_corpus.json", ["title", "extract"], ["Per capita indoor/outdoor usage fractions"])
    ]),

    # Domain 45
    ("45_housing_and_buildings", "Housing and buildings", "I", [
        ("45_01", "Rental housing and property features", "Property Management: Tenancy Agreements, Rent Regulations, and Amenities Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Renting",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Renting|Lease|Tenant|Landlord|Affordable_housing&format=json",
         "CC-BY-SA 4.0", "en", "json", "rental_housing_property_features_corpus.json", ["title", "extract"], ["Contractual lease mechanics and housing rights"]),
        ("45_02", "Building materials", "Civil Engineering: Structural Materials, Concrete, Steel, and Timber Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Building_material",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Building_material|Concrete|Structural_steel|Timber_framing|Masonry&format=json",
         "CC-BY-SA 4.0", "en", "json", "building_materials_engineering_corpus.json", ["title", "extract"], ["Compressive/tensile mechanical properties of building components"]),
        ("45_03", "Home energy efficiency", "Building Physics: Thermal Envelopes, Insulation, and Net-Zero Energy Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Low-energy_house",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Low-energy_house|Building_insulation|R-value_(insulation)|Heat_pump|Zero-energy_building&format=json",
         "CC-BY-SA 4.0", "en", "json", "home_energy_efficiency_corpus.json", ["title", "extract"], ["Thermal transmission coefficients and envelope sealing"]),
        ("45_04", "Maintenance and repair planning", "Facility Management: Preventative Lifecycle Schedules and Structural Inspection Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Facility_management",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Facility_management|Planned_maintenance|Roof|Structural_integrity_and_failure|Condition_monitoring&format=json",
         "CC-BY-SA 4.0", "en", "json", "building_maintenance_repair_planning_corpus.json", ["title", "extract"], ["Asset depreciation schedules and architectural inspection"])
    ]),

    # Domain 46
    ("46_travel_and_tourism", "Travel and tourism", "J", [
        ("46_01", "Destination descriptions", "Tourism Geography: World Heritage Sites, Eco-Tourism, and Landmarks Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Tourism",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Tourism|World_Heritage_Site|Ecotourism|Cultural_tourism|Tourist_attraction&format=json",
         "CC-BY-SA 4.0", "en", "json", "tourism_destination_descriptions_corpus.json", ["title", "extract"], ["Geographic destination profiles and cultural heritage"]),
        ("46_02", "Travel budgets and itineraries", "Travel Logistics: Backpacker Budgeting, Itinerary Structuring, and Passes Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Backpacking_(travel)",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Backpacking_(travel)|Itinerary|Travel_agency|Eurail|Travel_technology&format=json",
         "CC-BY-SA 4.0", "en", "json", "travel_budgets_itineraries_corpus.json", ["title", "extract"], ["Transit budgeting and route planning logistics"]),
        ("46_03", "Accommodation comparisons", "Hospitality Management: Hotels, Hostels, and Short-Term Rental Models Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Hotel",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Hotel|Hostel|Bed_and_breakfast|Short-term_rental|Hospitality_industry&format=json",
         "CC-BY-SA 4.0", "en", "json", "accommodation_comparisons_hospitality.json", ["title", "extract"], ["Lodging classifications and amenity benchmarking"]),
        ("46_04", "Travel reviews and visitor experiences", "Traveler Experience Studies, Cultural Tourism, and Review Systems Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Tripadvisor",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Tripadvisor|Online_travel_agency|Culture_shock|Travel_behavior|Tourist_gaze&format=json",
         "CC-BY-SA 4.0", "en", "json", "travel_reviews_visitor_experiences.json", ["title", "extract"], ["Ethnographic visitor perception and peer review heuristics"])
    ]),

    # Domain 47
    ("47_languages_and_communication", "Languages and communication", "J", [
        ("47_01", "Vocabulary and word meanings", "Linguistic Semantics, Lexicology, and WordNet Synsets Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Lexical_semantics",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Lexical_semantics|Synonym|Etymology|Morphology_(linguistics)|WordNet&format=json",
         "CC-BY-SA 4.0", "en", "json", "vocabulary_word_meanings_semantics.json", ["title", "extract"], ["Semantic relational taxonomies and etymological roots"]),
        ("47_02", "Grammar and sentence structure", "Theoretical Syntax, Generative Grammar, and Dependency Trees Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Syntax",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Syntax|Grammar|Clause|Subject%E2%80%93verb%E2%80%93object|Universal_grammar&format=json",
         "CC-BY-SA 4.0", "en", "json", "grammar_sentence_structure_syntax.json", ["title", "extract"], ["Syntactic constituency and grammatical inflections"]),
        ("47_03", "Translation and paraphrasing", "Translation Studies: Semantic Equivalence, Idioms, and Machine Translation Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Translation",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Translation|Machine_translation|Paraphrase|Idiom|BLEU&format=json",
         "CC-BY-SA 4.0", "en", "json", "translation_paraphrasing_studies_corpus.json", ["title", "extract"], ["Cross-lingual fidelity and idiomatic adaptation"]),
        ("47_04", "Written communication and comprehension", "Rhetoric, Discourse Analysis, and Written Communication Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Rhetoric",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Rhetoric|Discourse_analysis|Reading_comprehension|Expository_writing|Cohesion_(linguistics)&format=json",
         "CC-BY-SA 4.0", "en", "json", "written_communication_comprehension_corpus.json", ["title", "extract"], ["Rhetorical appeals and structural textual cohesion"])
    ]),

    # Domain 48
    ("48_human_behavior_and_psychology", "Human behavior and psychology", "J", [
        ("48_01", "Decision-making", "Behavioral Economics: Heuristics, Prospect Theory, and Biases Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Decision-making",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Decision-making|Prospect_theory|Heuristics_in_judgment_and_decision-making|Cognitive_bias|Bounded_rationality&format=json",
         "CC-BY-SA 4.0", "en", "json", "decision_making_behavioral_economics.json", ["title", "extract"], ["System 1 and System 2 cognitive processing frameworks"]),
        ("48_02", "Memory and attention", "Cognitive Psychology: Working Memory, Consolidation, and Attention Span Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Memory",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Memory|Working_memory|Attention|Long-term_memory|Forgetting_curve&format=json",
         "CC-BY-SA 4.0", "en", "json", "memory_attention_cognitive_psychology.json", ["title", "extract"], ["Atkinson-Shiffrin models and selective attentional filters"]),
        ("48_03", "Motivation and habits", "Motivation Theories: Self-Determination, Extrinsic Rewards, and Drive Theory Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Motivation",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Motivation|Self-determination_theory|Maslow%27s_hierarchy_of_needs|Extrinsic_motivation|Intrinsic_motivation&format=json",
         "CC-BY-SA 4.0", "en", "json", "motivation_habits_psychology_corpus.json", ["title", "extract"], ["Psychological needs and goal-directed human action"]),
        ("48_04", "Social interaction and group behavior", "Social Psychology: Group Polarization, Conformity, and Bystander Effect Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Social_psychology",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Social_psychology|Asch_conformity_experiments|Bystander_effect|Groupthink|In-group_and_out-group&format=json",
         "CC-BY-SA 4.0", "en", "json", "social_interaction_group_behavior.json", ["title", "extract"], ["Normative social influence and collective dynamics"])
    ]),

    # Domain 49
    ("49_relationships_and_family_life", "Relationships and family life", "J", [
        ("49_01", "Family communication", "Interpersonal Communication: Family Systems and Empathic Dialogue Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Interpersonal_communication",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Interpersonal_communication|Active_listening|Family_systems_theory|Nonviolent_Communication|Assertiveness&format=json",
         "CC-BY-SA 4.0", "en", "json", "family_communication_interpersonal_corpus.json", ["title", "extract"], ["Systemic familial patterns and nonviolent verbal structures"]),
        ("49_02", "Conflict resolution", "Conflict De-escalation: Principled Negotiation, Mediation, and Compromise Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Conflict_resolution",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Conflict_resolution|Mediation|Negotiation|De-escalation|Forgiveness&format=json",
         "CC-BY-SA 4.0", "en", "json", "conflict_resolution_mediation_corpus.json", ["title", "extract"], ["Harvard negotiation project and mediation protocols"]),
        ("49_03", "Parenting and child development", "Developmental Psychology: Attachment Theory, Parenting Styles, and Milestones Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Parenting",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Parenting|Attachment_theory|Child_development|Parenting_styles|Piaget%27s_theory_of_cognitive_development&format=json",
         "CC-BY-SA 4.0", "en", "json", "parenting_child_development_corpus.json", ["title", "extract"], ["Authoritative parenting and psychosocial stages of development"]),
        ("49_04", "Cooperation and interpersonal skills", "Prosocial Psychology: Reciprocity, Empathy, and Cooperative Problem Solving Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Prosocial_behavior",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Prosocial_behavior|Empathy|Altruism|Reciprocity_(social_psychology)|Cooperation&format=json",
         "CC-BY-SA 4.0", "en", "json", "cooperation_interpersonal_skills_corpus.json", ["title", "extract"], ["Evolutionary biology of mutual aid and interpersonal empathy"])
    ]),

    # Domain 50
    ("50_non_political_news_and_current_events", "Non-political news and current events", "J", [
        ("50_01", "Science and technology developments", "Science & Technology Journalism: Breakthroughs and Discoveries Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Science_journalism",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Science_journalism|James_Webb_Space_Telescope|Quantum_computing|Renewable_energy|CRISPR&format=json",
         "CC-BY-SA 4.0", "en", "json", "science_tech_news_developments_corpus.json", ["title", "extract"], ["Non-political empirical reporting on scientific research"]),
        ("50_02", "Environmental and weather reports", "Environmental Meteorology Reports: Ocean Anomaly and Ice Extent Updates Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Environmental_journalism",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Environmental_journalism|Weather_forecasting|Sea_ice|Ocean_temperature|Deforestation&format=json",
         "CC-BY-SA 4.0", "en", "json", "environmental_weather_reports_corpus.json", ["title", "extract"], ["Empirical meteorological and ecological event updates"]),
        ("50_03", "Sports news and match reports", "Sports Journalism: Athletic Tournaments and Championship Dispatches Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Sports_journalism",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Sports_journalism|Olympic_Games|World_Athletics_Championships|Paralympic_Games|Sports_broadcasting&format=json",
         "CC-BY-SA 4.0", "en", "json", "sports_news_match_reports_corpus.json", ["title", "extract"], ["Tournament recaps and athletic records reporting"]),
        ("50_04", "Health, education, and community announcements", "Public Health & Community Education Announcements Corpus",
         "Wikimedia Foundation", "https://en.wikipedia.org/wiki/Public_health",
         "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=Public_health|Health_literacy|Open_educational_resources|Community_health|Public_library&format=json",
         "CC-BY-SA 4.0", "en", "json", "health_education_community_announcements.json", ["title", "extract"], ["Civic education notices and community health directives"])
    ])
]

# Generate flat CATALOG list
CATALOG = []
for domain_id, domain_name, cat_code, subtopics in RAW_DOMAINS:
    cat_name = categories[cat_code]
    for sub_id, sub_name, cand_title, platform, src_url, dl_url, lic, lang, fmt, fn, tfields, limits in subtopics:
        CATALOG.append({
            "domain_id": domain_id,
            "domain_name": domain_name,
            "category": cat_name,
            "subtopic_id": sub_id,
            "subtopic_name": sub_name,
            "candidate_title": cand_title,
            "source_platform": platform,
            "publisher": platform + " Contributor Community",
            "source_url": src_url,
            "download_url": dl_url,
            "license": lic,
            "language": lang,
            "format": fmt,
            "target_filename": fn,
            "text_fields": tfields,
            "limitations": limits
        })

print(f"Total subtopics configured: {len(CATALOG)}")
assert len(CATALOG) == 200, f"Expected 200, got {len(CATALOG)}"

with open("catalog_definitions.py", "w", encoding="utf-8") as f:
    f.write("# catalog_definitions.py\n")
    f.write("# Complete verified 200-subtopic catalog definitions across 50 domains\n\n")
    f.write("CATALOG = " + json.dumps(CATALOG, indent=4) + "\n")

print("catalog_definitions.py successfully written.")
