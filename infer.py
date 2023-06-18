"""
This code a slight modification of perplexity by hugging face
https://huggingface.co/docs/transformers/perplexity

Both this code and the orignal code are published under the MIT license.

by Burhan Ul tayyab and Nicholas Chua
"""

from model import GPT2PPLV2 as GPT2PPL

# initialize the model
model = GPT2PPL()

sentence = """The game called Elden Ring has been generating a lot of buzz among gamers and fantasy enthusiasts alike. It brings together the creative genius of Hidetaka Miyazaki, the creator of the acclaimed Dark Souls series, and celebrated author George R.R. Martin, known for his epic fantasy novels like A Song of Ice and Fire. Elden Ring presents players with a richly crafted world that is both familiar and distinct. The combination of dark fantasy elements with the immersive storytelling that Martin is renowned for creates a unique gaming experience that pushes boundaries and captivates players from start to finish. One noteworthy aspect of Elden Ring is its intricate lore. As players progress through the game, they uncover an extensive backstory filled with hidden details and complex characters. This depth adds layers to the overall narrative, allowing players to fully immerse themselves in this captivating world. From ancient ruins to towering castles, each location tells its own story, contributing to an interconnected web of lore that unfolds gradually throughout the game. Furthermore, Elden Ring raises the bar when it comes to combat mechanics. Miyazaki's signature challenging gameplay style shines brightly here as well – precise timing and strategizing are key components in overcoming formidable adversaries scattered throughout the game world. From colossal bosses to hordes of ruthless enemies, each encounter tests players' skills while rewarding their perseverance in equal measure. Additionally, one cannot overlook the breathtaking visuals in Elden Ring. The attention to detail is remarkable; every blade of grass sways convincingly in the wind, while sunsets bathe landscapes in golden hues that evoke a sense of awe and wonderment. Coupled with a hauntingly beautiful soundtrack composed by Yuka Kitamura (known for her work on other FromSoftware games), these visuals contribute greatly to crafting an atmospheric experience unlike any other. FromSoftware has consistently delivered games with high replayability value, allowing players multiple paths through different play styles or character builds. Elden Ring promises to uphold this tradition with a vast array of customization options, encouraging players to explore different strategies and experiment with various combinations. This ensures that no two playthroughs are the same, keeping the game fresh and exciting even after countless hours of gameplay. In conclusion, Elden Ring represents a collaboration of remarkable talent resulting in a game that is anticipated to be nothing short of extraordinary. With its meticulously crafted lore, challenging combat mechanics, stunning visuals, and replayability value, it promises an immersive experience that will leave players wanting more. Whether you are a longtime fan of FromSoftware or someone seeking their next great gaming adventure, Elden Ring is sure to captivate your imagination and transport you to a world like no other."""

model(sentence, 100, "v1.0")
