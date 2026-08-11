import asyncio
from googletrans import Translator

async def main():
    translator = Translator()
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    translated = await translator.translate(french_words, src='fr', dest='en')

    print("French Words:", french_words)
    print("Translated Words:", [t.text for t in translated])

asyncio.run(main())