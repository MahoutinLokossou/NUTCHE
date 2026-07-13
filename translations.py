# translations.py
# Simple in-memory translation dictionary for NUTCHE Enterprise (Farine Mon Choix).
# Keys are dotted "section.item" strings, looked up at render time
# via the `t()` helper injected into every template (see app.py).

TRANSLATIONS = {
    "fr": {
        # --- Site-wide ---
        "site.name": "NUTCHE",
        "site.tagline": "Le choix nutritionnel de toute la famille",

        # --- Navbar ---
        "nav.home": "Accueil",
        "nav.about": "À propos",
        "nav.products": "Produit",
        "nav.benefits": "Avantages",
        "nav.services": "Nos activités",
        "nav.gallery": "Galerie",
        "nav.contact": "Contact",
        "nav.cta": "Demander une consultation",

        # --- Hero (home) ---
        "hero.eyebrow": "FARINE MON CHOIX — tout sur la farine composée",
        "hero.title": "NUTCHE : le choix nutritionnel de toute la famille",
        "hero.subtitle": (
            "NUTCHE Enterprise produit Farine Mon Choix, une farine composée nutritive à base de "
            "maïs, soja, arachide et sorgho cultivés localement au Bénin — abordable, saine et "
            "pensée pour toute la famille."
        ),
        "hero.cta_primary": "Découvrir le produit",
        "hero.cta_secondary": "Nos activités",
        "hero.ingredients_label": "Composé de 4 cultures locales",

        # --- Home page sections ---
        "home.pillars.title": "Trois piliers, une seule mission",
        "home.pillar1.title": "Innovation alimentaire",
        "home.pillar1.text": (
            "Développer des aliments abordables, sûrs et riches en nutriments à partir d'ingrédients "
            "locaux, pour les nourrissons, jeunes enfants, femmes enceintes et allaitantes."
        ),
        "home.pillar2.title": "Recherche & savoir",
        "home.pillar2.text": (
            "Faire progresser des solutions fondées sur des preuves en matière de sécurité, de "
            "qualité et de nutrition, avec universités, chercheurs et communautés."
        ),
        "home.pillar3.title": "Communauté & systèmes alimentaires",
        "home.pillar3.text": (
            "Renforcer la sécurité alimentaire des ménages par l'éducation nutritionnelle, les "
            "démonstrations culinaires et des partenariats pour une agriculture durable."
        ),
        "home.why.title": "Pourquoi une farine composée ?",
        "home.why.text": (
            "En combinant maïs, soja, arachide et sorgho cultivés par de petits exploitants béninois, "
            "Farine Mon Choix apporte protéines, énergie et micronutriments essentiels aux enfants en "
            "croissance et aux mères allaitantes, tout en soutenant les filières agricoles locales."
        ),
        "home.stats.farmers": "Petits exploitants partenaires",
        "home.stats.trained": "Personnes sensibilisées à la nutrition",
        "home.stats.blends": "Cultures locales valorisées",

        # --- About ---
        "about.title": "À propos de NUTCHE",
        "about.intro": (
            "Une entreprise sociale béninoise dédiée à la nutrition, qui transforme des ingrédients "
            "locaux en solutions durables pour la sécurité alimentaire."
        ),
        "about.who.title": "Qui sommes-nous",
        "about.who.text": (
            "NUTCHE Enterprise est une entreprise sociale à vocation nutritionnelle basée au Bénin, "
            "engagée à améliorer la sécurité alimentaire, la nutrition et les moyens de subsistance "
            "grâce à des solutions alimentaires innovantes, abordables et d'origine locale. Fondée "
            "par Mèdédodé Monique Sognigbe, spécialiste en sécurité alimentaire et nutrition "
            "communautaire, NUTCHE a été créée pour répondre au défi persistant de l'accès limité à "
            "des aliments sûrs, nutritifs, abordables et culturellement acceptés dans les communautés "
            "africaines."
        ),
        "about.approach.title": "Notre approche",
        "about.approach.text": (
            "Nous croyons que des solutions durables à la malnutrition commencent par les ressources "
            "locales et l'innovation portée par les communautés. Nous transformons des produits "
            "agricoles disponibles localement en aliments nutritifs de haute qualité qui améliorent "
            "la diversité alimentaire, renforcent la nutrition des ménages et créent des opportunités "
            "économiques pour les petits exploitants, les femmes et les jeunes."
        ),
        "about.mission.title": "Notre mission",
        "about.mission.text": (
            "Améliorer la nutrition et la sécurité alimentaire en développant des solutions "
            "alimentaires innovantes, en faisant progresser la recherche et en donnant aux "
            "communautés les moyens de construire des systèmes alimentaires résilients et durables."
        ),
        "about.vision.title": "Notre vision",
        "about.vision.text": (
            "Un avenir où chaque foyer a accès à des aliments sûrs, nutritifs, abordables et "
            "produits de façon durable."
        ),
        "about.values.title": "Nos valeurs",
        "about.value1": "Innovation",
        "about.value2": "Intégrité",
        "about.value3": "Excellence scientifique",
        "about.value4": "Durabilité",
        "about.value5": "Autonomisation des communautés",
        "about.value6": "Collaboration",
        "about.value7": "Inclusion",

        # --- Products ---
        "products.title": "Farine Mon Choix",
        "products.intro": "Une seule farine, quatre cultures, toute une famille nourrie.",
        "products.tagline": "FARINE MON CHOIX",
        "products.short_desc": "Une composition de farine de maïs, soja, arachide et sorgho.",
        "products.long_title": "Farine Mon Choix",
        "products.long_desc": (
            "Farine Mon Choix associe maïs, soja, arachide et sorgho — quatre cultures cultivées par "
            "de petits exploitants au Bénin — en une seule farine dense en nutriments. Elle est "
            "moulue pour rester abordable au quotidien tout en apportant les protéines, l'énergie et "
            "les micronutriments dont les enfants en croissance et les mères allaitantes ont le plus "
            "besoin."
        ),
        "products.ingredients_title": "Ce qu'elle contient",
        "products.ingredient1": "Maïs",
        "products.ingredient2": "Soja",
        "products.ingredient3": "Arachide",
        "products.ingredient4": "Sorgho",
        "products.request": "Demander un échantillon",

        # --- Benefits ---
        "benefits.title": "Pourquoi choisir notre farine composée ?",
        "benefits.intro": "Cinq raisons pour lesquelles les familles béninoises font confiance à Farine Mon Choix.",
        "benefits.item1": "Riche en nutriments et en protéines",
        "benefits.item2": "Soutient les agriculteurs locaux",
        "benefits.item3": "Abordable et saine",
        "benefits.item4": "Adaptée à la pâtisserie et à la cuisine",
        "benefits.item5": "Favorise la sécurité alimentaire",

        # --- Services / Activities ---
        "services.title": "Nos activités",
        "services.intro": "Ce que fait NUTCHE Enterprise, du champ à la table familiale.",
        "services.training.title": "Éducation nutritionnelle",
        "services.training.text": (
            "Démonstrations culinaires communautaires et formations sur la sécurité, la qualité et "
            "une alimentation saine."
        ),
        "services.consulting.title": "Recherche & collaboration",
        "services.consulting.text": (
            "Partenariats avec universités et chercheurs pour produire des données probantes qui "
            "orientent le développement de nos produits et des politiques publiques."
        ),
        "services.book": "Nous contacter",
        "services.format.title": "Nos quatre activités",
        "services.format1": "Développement de produits — formulation et test de farines composées denses en nutriments",
        "services.format2": "Partenariats agricoles — approvisionnement direct auprès des coopératives de petits exploitants, femmes et jeunes",
        "services.format3": "Éducation nutritionnelle — démonstrations culinaires et formation communautaire",
        "services.format4": "Recherche collaborative — partenariats avec universités et chercheurs",

        # --- Gallery ---
        "gallery.title": "Galerie",
        "gallery.intro": "Un aperçu de notre production, nos formations et nos produits.",
        "gallery.filter.all": "Tout",
        "gallery.filter.production": "Production",
        "gallery.filter.training": "Formations",
        "gallery.filter.products": "Produits",

        # --- Contact ---
        "contact.title": "Contactez-nous",
        "contact.intro": "Une question sur Farine Mon Choix, une formation ou une consultation ? Écrivez-nous.",
        "contact.form.name": "Nom complet",
        "contact.form.email": "Adresse e-mail",
        "contact.form.phone": "Téléphone",
        "contact.form.subject": "Sujet",
        "contact.form.subject.product": "Question sur le produit",
        "contact.form.subject.training": "Formation",
        "contact.form.subject.consultation": "Consultation",
        "contact.form.subject.other": "Autre",
        "contact.form.message": "Votre message",
        "contact.form.submit": "Envoyer le message",
        "contact.form.error": "Merci de remplir tous les champs obligatoires.",
        "contact.form.send_error": "Désolé, une erreur est survenue lors de l'envoi. Merci de réessayer ou de nous écrire directement à nutcheproducts@gmail.com.",
        "contact.form.success": "Merci ! Votre message a bien été envoyé, nous vous répondrons rapidement.",
        "contact.info.title": "Nos coordonnées",
        "contact.info.address": "Adresse",
        "contact.info.phone": "Téléphone",
        "contact.info.email": "E-mail",
        "contact.info.hours": "Heures d'ouverture",
        "contact.info.hours.value": "Lundi – Vendredi, 8h00 – 17h00",
        "contact.info.address.value": "Commune d'Adjarra, Bénin",
        "contact.info.phone.value": "+229 01 41 232945",
        "contact.info.email.value": "nutcheproducts@gmail.com",

        # --- Footer ---
        "footer.tagline": "Farine Mon Choix — tout sur la farine composée.",
        "footer.links.title": "Liens rapides",
        "footer.contact.title": "Contact",
        "footer.social.title": "Suivez-nous",
        "footer.rights": "Tous droits réservés.",

        # --- Language switcher ---
        "lang.switch": "English",
    },
    "en": {
        # --- Site-wide ---
        "site.name": "NUTCHE",
        "site.tagline": "Nutritional Choice of the Whole Family",

        # --- Navbar ---
        "nav.home": "Home",
        "nav.about": "About",
        "nav.products": "Product",
        "nav.benefits": "Benefits",
        "nav.services": "Activities",
        "nav.gallery": "Gallery",
        "nav.contact": "Contact",
        "nav.cta": "Request a consultation",

        # --- Hero (home) ---
        "hero.eyebrow": "FARINE MON CHOIX — all about composite flour",
        "hero.title": "NUTCHE: Nutritional Choice of the Whole Family",
        "hero.subtitle": (
            "NUTCHE Enterprise produces Farine Mon Choix, a nutritious composite flour made from "
            "maize, soya, groundnuts and sorghum grown locally in Benin — affordable, healthy, and "
            "made for the whole family."
        ),
        "hero.cta_primary": "Discover the product",
        "hero.cta_secondary": "Our activities",
        "hero.ingredients_label": "Made from 4 local crops",

        # --- Home page sections ---
        "home.pillars.title": "Three pillars, one mission",
        "home.pillar1.title": "Nutritious Food Innovation",
        "home.pillar1.text": (
            "Developing affordable, safe and nutrient-dense food products using indigenous "
            "ingredients for infants, young children, pregnant women and lactating mothers."
        ),
        "home.pillar2.title": "Research & Knowledge",
        "home.pillar2.text": (
            "Advancing evidence-based solutions in food safety, quality and nutrition, working with "
            "universities, researchers and communities."
        ),
        "home.pillar3.title": "Community & Food Systems",
        "home.pillar3.text": (
            "Strengthening household food security through nutrition education, food demonstrations "
            "and partnerships for sustainable agriculture."
        ),
        "home.why.title": "Why composite flour?",
        "home.why.text": (
            "By blending maize, soya, groundnuts and sorghum grown by smallholder farmers in Benin, "
            "Farine Mon Choix delivers the protein, energy and micronutrients growing children and "
            "nursing mothers need most, while supporting local agricultural value chains."
        ),
        "home.stats.farmers": "Partner smallholder farmers",
        "home.stats.trained": "People reached through nutrition education",
        "home.stats.blends": "Local crops put to work",

        # --- About ---
        "about.title": "About NUTCHE",
        "about.intro": (
            "A nutrition-focused social enterprise from Benin, turning local ingredients into "
            "lasting solutions for food security."
        ),
        "about.who.title": "Who We Are",
        "about.who.text": (
            "NUTCHE Enterprise is a nutrition-focused social enterprise based in Benin, committed to "
            "improving food security, nutrition and livelihoods through innovative, affordable and "
            "locally sourced food solutions. Founded by Mèdédodé Monique Sognigbe, a Food Security "
            "and Community Nutrition specialist, NUTCHE was established to address the persistent "
            "challenge of limited access to safe, nutritious, affordable and culturally acceptable "
            "foods across African communities."
        ),
        "about.approach.title": "Our Approach",
        "about.approach.text": (
            "We believe that sustainable solutions to malnutrition begin with local resources and "
            "community-driven innovation. We transform locally available agricultural products into "
            "high-quality, nutrient-rich foods that improve dietary diversity, enhance household "
            "nutrition and create economic opportunities for smallholder farmers, women and youth."
        ),
        "about.mission.title": "Our Mission",
        "about.mission.text": (
            "To improve nutrition and food security by developing innovative food solutions, "
            "advancing research and empowering communities to build resilient, sustainable food "
            "systems."
        ),
        "about.vision.title": "Our Vision",
        "about.vision.text": (
            "A future where every household has access to safe, nutritious, affordable and "
            "sustainably produced foods."
        ),
        "about.values.title": "Our Values",
        "about.value1": "Innovation",
        "about.value2": "Integrity",
        "about.value3": "Scientific Excellence",
        "about.value4": "Sustainability",
        "about.value5": "Community Empowerment",
        "about.value6": "Collaboration",
        "about.value7": "Inclusion",

        # --- Products ---
        "products.title": "Farine Mon Choix",
        "products.intro": "One flour, four crops, a whole family nourished.",
        "products.tagline": "FARINE MON CHOIX",
        "products.short_desc": "A composition of maize, soya, groundnut and sorghum flour.",
        "products.long_title": "Farine Mon Choix",
        "products.long_desc": (
            "Farine Mon Choix blends maize, soya, groundnuts and sorghum — four crops grown by "
            "smallholder farmers in Benin — into a single nutrient-dense flour. It is milled to be "
            "affordable for everyday households while delivering the protein, energy and "
            "micronutrients growing children and nursing mothers need most."
        ),
        "products.ingredients_title": "What's inside",
        "products.ingredient1": "Maize",
        "products.ingredient2": "Soya",
        "products.ingredient3": "Groundnut",
        "products.ingredient4": "Sorghum",
        "products.request": "Request a sample",

        # --- Benefits ---
        "benefits.title": "Why Choose Our Composite Flour?",
        "benefits.intro": "Five reasons families across Benin trust Farine Mon Choix.",
        "benefits.item1": "Rich in nutrients and protein",
        "benefits.item2": "Supports local farmers",
        "benefits.item3": "Affordable and healthy",
        "benefits.item4": "Suitable for baking and cooking",
        "benefits.item5": "Promotes food security",

        # --- Services / Activities ---
        "services.title": "Our Activities",
        "services.intro": "What NUTCHE Enterprise does, from the field to the family table.",
        "services.training.title": "Nutrition Education",
        "services.training.text": (
            "Running community food demonstrations and training on food safety, quality and "
            "healthy diets."
        ),
        "services.consulting.title": "Research Collaboration",
        "services.consulting.text": (
            "Partnering with universities and researchers to generate evidence that guides product "
            "and policy development."
        ),
        "services.book": "Get in touch",
        "services.format.title": "Our Four Activities",
        "services.format1": "Product Development — formulating and testing nutrient-dense composite flours",
        "services.format2": "Farmer Partnerships — sourcing directly from smallholder, women and youth cooperatives",
        "services.format3": "Nutrition Education — community food demonstrations and training",
        "services.format4": "Research Collaboration — partnerships with universities and researchers",

        # --- Gallery ---
        "gallery.title": "Gallery",
        "gallery.intro": "A look inside our production, trainings and products.",
        "gallery.filter.all": "All",
        "gallery.filter.production": "Production",
        "gallery.filter.training": "Trainings",
        "gallery.filter.products": "Products",

        # --- Contact ---
        "contact.title": "Get in touch",
        "contact.intro": "A question about Farine Mon Choix, a training or a consultation? Write to us.",
        "contact.form.name": "Full name",
        "contact.form.email": "Email address",
        "contact.form.phone": "Phone",
        "contact.form.subject": "Subject",
        "contact.form.subject.product": "Product question",
        "contact.form.subject.training": "Training",
        "contact.form.subject.consultation": "Consultation",
        "contact.form.subject.other": "Other",
        "contact.form.message": "Your message",
        "contact.form.submit": "Send message",
        "contact.form.error": "Please fill in all required fields.",
        "contact.form.send_error": "Sorry, something went wrong while sending your message. Please try again or email us directly at nutcheproducts@gmail.com.",
        "contact.form.success": "Thank you! Your message has been sent, we'll get back to you shortly.",
        "contact.info.title": "Our details",
        "contact.info.address": "Address",
        "contact.info.phone": "Phone",
        "contact.info.email": "Email",
        "contact.info.hours": "Opening hours",
        "contact.info.hours.value": "Monday – Friday, 8:00 AM – 5:00 PM",
        "contact.info.address.value": "Adjarra Municipality, Benin",
        "contact.info.phone.value": "+229 01 41 232945",
        "contact.info.email.value": "nutcheproducts@gmail.com",

        # --- Footer ---
        "footer.tagline": "Farine Mon Choix — all about composite flour.",
        "footer.links.title": "Quick links",
        "footer.contact.title": "Contact",
        "footer.social.title": "Follow us",
        "footer.rights": "All rights reserved.",

        # --- Language switcher ---
        "lang.switch": "Français",
    },
}


def translate(key: str, lang: str) -> str:
    """Look up `key` for `lang`, falling back to French, then to the key itself."""
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS["fr"])
    if key in lang_dict:
        return lang_dict[key]
    return TRANSLATIONS["fr"].get(key, key)