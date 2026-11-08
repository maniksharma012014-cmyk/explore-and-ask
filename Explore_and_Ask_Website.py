# EXPLORE & ASK — Python Website

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import socket
import webbrowser
import threading
import time
import os

PORT = int(os.environ.get("PORT", "8000"))
PUBLIC_URL = ""

QUESTIONS = [
  {
    "id": 1,
    "section": "Japan",
    "question": "What is the capital of Japan?",
    "answer": "Tokyo is the capital city of Japan. It is famous for modern buildings, technology, shopping centres and busy streets."
  },
  {
    "id": 2,
    "section": "Japan",
    "question": "What is the currency of Japan?",
    "answer": "The currency of Japan is the Japanese yen. Its symbol is ¥."
  },
  {
    "id": 3,
    "section": "Japan",
    "question": "Which language is spoken in Japan?",
    "answer": "Japanese is the main language spoken in Japan. It uses Hiragana, Katakana and Kanji writing systems."
  },
  {
    "id": 4,
    "section": "Japan",
    "question": "What is Japan famous for?",
    "answer": "Japan is famous for technology, anime, sushi, cherry blossoms, bullet trains and traditional culture."
  },
  {
    "id": 5,
    "section": "Japan",
    "question": "What does the Japanese flag represent?",
    "answer": "The Japanese flag has a red circle on a white background. The circle represents the sun, and Japan is often called the Land of the Rising Sun."
  },
  {
    "id": 6,
    "section": "Japan",
    "question": "What are Japan's four main islands?",
    "answer": "Japan's four main islands are Honshu, Hokkaido, Kyushu and Shikoku. Honshu is the largest."
  },
  {
    "id": 7,
    "section": "Japan",
    "question": "What is Mount Fuji?",
    "answer": "Mount Fuji is Japan's highest mountain, about 3,776 metres tall. It is a famous volcanic mountain and a symbol of Japan."
  },
  {
    "id": 8,
    "section": "Japan",
    "question": "What is the population of Japan?",
    "answer": "Japan has approximately 123 million people according to recent estimates. Its population is decreasing because of low birth rates and an ageing population."
  },
  {
    "id": 9,
    "section": "Japan",
    "question": "Which is the largest city in Japan?",
    "answer": "Tokyo is Japan's largest city and the centre of its biggest metropolitan area. It is famous for business, transport and entertainment."
  },
  {
    "id": 10,
    "section": "Japan",
    "question": "Where is Japan located?",
    "answer": "Japan is an island country in East Asia, in the Pacific Ocean. It lies east of China and the Korean Peninsula."
  },
  {
    "id": 11,
    "section": "Japan",
    "question": "What are cherry blossoms?",
    "answer": "Cherry blossoms are pink and white flowers of cherry trees. They usually bloom in spring and are loved throughout Japan."
  },
  {
    "id": 12,
    "section": "Japan",
    "question": "What is Hanami?",
    "answer": "Hanami is the Japanese tradition of enjoying cherry blossoms. People gather in parks with family and friends to admire the flowers."
  },
  {
    "id": 13,
    "section": "Japan",
    "question": "What is sushi?",
    "answer": "Sushi is a Japanese dish usually made with vinegared rice. It may include seafood, vegetables and other ingredients."
  },
  {
    "id": 14,
    "section": "Japan",
    "question": "What is ramen?",
    "answer": "Ramen is a popular Japanese noodle soup. It usually contains noodles, flavourful broth and toppings such as eggs or vegetables."
  },
  {
    "id": 15,
    "section": "Japan",
    "question": "What is tempura?",
    "answer": "Tempura is a Japanese dish made by coating seafood or vegetables in a light batter and frying them until crisp."
  },
  {
    "id": 16,
    "section": "Japan",
    "question": "What is a kimono?",
    "answer": "A kimono is a traditional Japanese garment with long sleeves and a wraparound design. It is often worn on special occasions."
  },
  {
    "id": 17,
    "section": "Japan",
    "question": "What is origami?",
    "answer": "Origami is the Japanese art of paper folding. People make shapes such as birds, flowers and animals."
  },
  {
    "id": 18,
    "section": "Japan",
    "question": "What is anime?",
    "answer": "Anime is a style of animated entertainment developed in Japan. It includes films and television series for different age groups."
  },
  {
    "id": 19,
    "section": "Japan",
    "question": "What is manga?",
    "answer": "Manga refers to Japanese comic books and graphic novels. They cover subjects such as adventure, sports and fantasy."
  },
  {
    "id": 20,
    "section": "Japan",
    "question": "What is sumo wrestling?",
    "answer": "Sumo is a traditional Japanese sport in which two wrestlers compete inside a circular ring. The aim is to push the opponent out or make them touch the ground."
  },
  {
    "id": 21,
    "section": "Japan",
    "question": "What is the Shinkansen?",
    "answer": "The Shinkansen is Japan's high-speed railway system, commonly called the bullet train. It connects major cities."
  },
  {
    "id": 22,
    "section": "Japan",
    "question": "Why is Japan famous for technology?",
    "answer": "Japan is famous for advanced technology, electronics, robotics, vehicles and engineering. Japanese companies make many products used around the world."
  },
  {
    "id": 23,
    "section": "Japan",
    "question": "What is Tokyo famous for?",
    "answer": "Tokyo is famous for tall buildings, busy crossings, shopping areas, restaurants and modern transport. It also has historic temples and parks."
  },
  {
    "id": 24,
    "section": "Japan",
    "question": "What is Kyoto famous for?",
    "answer": "Kyoto is famous for historic temples, traditional gardens and cultural heritage. It was once the capital of Japan."
  },
  {
    "id": 25,
    "section": "Japan",
    "question": "What is Osaka famous for?",
    "answer": "Osaka is famous for street food, entertainment and friendly people. Osaka Castle and Universal Studios Japan are popular attractions."
  },
  {
    "id": 26,
    "section": "Japan",
    "question": "What are Shinto shrines?",
    "answer": "Shinto shrines are sacred places where people practise Japan's traditional Shinto religion. They are often dedicated to spirits called kami."
  },
  {
    "id": 27,
    "section": "Japan",
    "question": "What is a torii gate?",
    "answer": "A torii is a traditional Japanese gate usually found at the entrance to a Shinto shrine. It marks the entrance to a sacred area."
  },
  {
    "id": 28,
    "section": "Japan",
    "question": "What is the Japanese tea ceremony?",
    "answer": "The Japanese tea ceremony is a traditional way of preparing and serving matcha tea. It values respect, calmness and careful movements."
  },
  {
    "id": 29,
    "section": "Japan",
    "question": "What is matcha?",
    "answer": "Matcha is a finely ground powder made from specially grown green tea leaves. It is used in tea and sweets."
  },
  {
    "id": 30,
    "section": "Japan",
    "question": "How is New Year celebrated in Japan?",
    "answer": "New Year is an important celebration in Japan. Families clean their homes, eat special food and visit temples or shrines."
  }
]
QUESTIONS.extend([
  {
    "id": 31,
    "section": "Japan",
    "question": "What is the Obon festival?",
    "answer": "Obon is a Japanese festival that honours the spirits of ancestors. Families remember loved ones and take part in traditional activities."
  },
  {
    "id": 32,
    "section": "Japan",
    "question": "What is Golden Week?",
    "answer": "Golden Week is a holiday period from late April to early May. Many people travel or spend time with family."
  },
  {
    "id": 33,
    "section": "Japan",
    "question": "How is Children's Day celebrated in Japan?",
    "answer": "Children's Day is celebrated on 5 May. Families display colourful carp-shaped windsocks called koinobori to wish children happiness and good health."
  },
  {
    "id": 34,
    "section": "Japan",
    "question": "Who were the samurai?",
    "answer": "Samurai were members of Japan's warrior class in the past. They served powerful leaders and valued loyalty, discipline and courage."
  },
  {
    "id": 35,
    "section": "Japan",
    "question": "What was the Edo period?",
    "answer": "The Edo period lasted from 1603 to 1868 under the Tokugawa shogunate. It was a time of peace, economic growth and cultural development."
  },
  {
    "id": 36,
    "section": "Japan",
    "question": "What was the Meiji Restoration?",
    "answer": "The Meiji Restoration began in 1868 and restored political power to the emperor. Japan then modernised its government, industries and education."
  },
  {
    "id": 37,
    "section": "Japan",
    "question": "What is Kabuki theatre?",
    "answer": "Kabuki is a traditional Japanese theatre form known for colourful costumes, music and dramatic acting. It presents stories about history and society."
  },
  {
    "id": 38,
    "section": "Japan",
    "question": "Which sports are popular in Japan?",
    "answer": "Baseball, football, sumo wrestling, judo, karate and tennis are popular sports in Japan."
  },
  {
    "id": 39,
    "section": "Japan",
    "question": "Why do earthquakes occur in Japan?",
    "answer": "Japan lies near the boundaries of several tectonic plates. Their movement can release energy and cause earthquakes."
  },
  {
    "id": 40,
    "section": "Japan",
    "question": "What is the Pacific Ring of Fire?",
    "answer": "The Pacific Ring of Fire is a large area around the Pacific Ocean where many earthquakes and volcanic eruptions occur. Japan lies within this region."
  },
  {
    "id": 41,
    "section": "Japan",
    "question": "What is a tsunami?",
    "answer": "A tsunami is a series of powerful ocean waves usually caused by an underwater earthquake, volcanic eruption or landslide."
  },
  {
    "id": 42,
    "section": "Japan",
    "question": "How does Japan prepare for earthquakes?",
    "answer": "Japan uses earthquake drills, early-warning systems, safety education and strong building standards to reduce earthquake damage."
  },
  {
    "id": 43,
    "section": "Japan",
    "question": "What is a typhoon?",
    "answer": "A typhoon is a powerful tropical storm that forms over the northwestern Pacific Ocean. It can bring strong winds and heavy rain."
  },
  {
    "id": 44,
    "section": "Japan",
    "question": "What is the climate of Japan?",
    "answer": "Japan has different climates. Northern areas have cold, snowy winters, while southern areas are generally warmer and more humid."
  },
  {
    "id": 45,
    "section": "Japan",
    "question": "Which animals are found in Japan?",
    "answer": "Animals found in Japan include Japanese macaques, deer, foxes, bears and many kinds of birds."
  },
  {
    "id": 46,
    "section": "Japan",
    "question": "What are Japanese gardens famous for?",
    "answer": "Japanese gardens are famous for their peaceful beauty. They often contain rocks, ponds, bridges, trees and carefully arranged plants."
  },
  {
    "id": 47,
    "section": "Japan",
    "question": "What are Japanese school uniforms like?",
    "answer": "Many Japanese schools have uniforms. Common styles include shirts, trousers, skirts, jackets and sailor-style uniforms."
  },
  {
    "id": 48,
    "section": "Japan",
    "question": "What does bowing mean in Japanese culture?",
    "answer": "Bowing is a Japanese custom used to show respect, politeness and gratitude. People bow when greeting, thanking or apologising."
  },
  {
    "id": 49,
    "section": "Japan",
    "question": "What are famous tourist attractions in Japan?",
    "answer": "Famous attractions include Mount Fuji, Tokyo Tower, Kyoto's temples, Osaka Castle and Hiroshima Peace Memorial Park."
  },
  {
    "id": 50,
    "section": "Japan",
    "question": "Why should people visit Japan?",
    "answer": "People should visit Japan to enjoy its beautiful scenery, history, delicious food and unique traditions. It also has modern cities and excellent transport."
  },
  {
    "id": 51,
    "section": "Japan",
    "question": "What is Hokkaido famous for?",
    "answer": "Hokkaido is Japan's northernmost main island. It is famous for snowy winters, ski resorts, national parks and seafood."
  },
  {
    "id": 52,
    "section": "Japan",
    "question": "What is Okinawa famous for?",
    "answer": "Okinawa is famous for warm weather, beautiful beaches, clear blue water and its unique island culture."
  },
  {
    "id": 53,
    "section": "Japan",
    "question": "What is Japan's traditional national sport?",
    "answer": "Sumo wrestling is widely regarded as Japan's traditional national sport. It has a long history and cultural importance."
  },
  {
    "id": 54,
    "section": "Japan",
    "question": "What is a bullet train?",
    "answer": "A bullet train is a high-speed passenger train. Japan's Shinkansen is one of the world's best-known bullet train systems."
  },
  {
    "id": 55,
    "section": "Japan",
    "question": "What does the word sakura mean?",
    "answer": "Sakura is the Japanese word for cherry blossoms. These flowers are associated with spring and beauty."
  },
  {
    "id": 56,
    "section": "Japan",
    "question": "What is a Japanese onsen?",
    "answer": "An onsen is a natural hot spring in Japan. People visit onsen baths to relax in naturally heated mineral water."
  },
  {
    "id": 57,
    "section": "Japan",
    "question": "What is a Japanese pagoda?",
    "answer": "A Japanese pagoda is a tower-like structure often found at Buddhist temples. It usually has several roofs and traditional architecture."
  },
  {
    "id": 58,
    "section": "Japan",
    "question": "Why is Mount Fuji important in Japanese culture?",
    "answer": "Mount Fuji is an important symbol of Japan. It has inspired artists, poets and travellers and is considered sacred in Japanese traditions."
  },
  {
    "id": 59,
    "section": "Japan",
    "question": "What are some famous Japanese inventions?",
    "answer": "Japan has contributed inventions and innovations such as the QR code and advances in electronics, robotics and high-speed rail technology."
  },
  {
    "id": 60,
    "section": "Japan",
    "question": "How does Japan protect its environment?",
    "answer": "Japan protects its environment through recycling, waste separation, conservation areas and pollution-control rules."
  }
])
QUESTIONS.extend([
  {
    "id": 61,
    "section": "Udhampur",
    "question": "Where is Udhampur located?",
    "answer": "Udhampur is a town and district in the Jammu region of Jammu and Kashmir, India. It is surrounded by hills and mountains."
  },
  {
    "id": 62,
    "section": "Udhampur",
    "question": "In which Union Territory is Udhampur situated?",
    "answer": "Udhampur is situated in the Union Territory of Jammu and Kashmir in northern India. It is part of the Jammu division."
  },
  {
    "id": 63,
    "section": "Udhampur",
    "question": "What is the headquarters of Udhampur district?",
    "answer": "Udhampur city is the administrative headquarters of Udhampur district. Important government offices are located there."
  },
  {
    "id": 64,
    "section": "Udhampur",
    "question": "What is Udhampur famous for?",
    "answer": "Udhampur is famous for beautiful mountains, temples, Dogra culture and traditional food. It is also known for the Krimchi temples and Ramnagar Fort."
  },
  {
    "id": 65,
    "section": "Udhampur",
    "question": "Which languages are spoken in Udhampur?",
    "answer": "Dogri is widely spoken in Udhampur, along with Hindi, Urdu and other local languages. English is also used in schools and official communication."
  },
  {
    "id": 66,
    "section": "Udhampur",
    "question": "What is the climate of Udhampur?",
    "answer": "Udhampur generally has hot summers and cool winters. Higher mountain areas are cooler, and the region receives rainfall during the monsoon."
  },
  {
    "id": 67,
    "section": "Udhampur",
    "question": "What is Patnitop?",
    "answer": "Patnitop is a beautiful hill destination in the Jammu region. It is known for green forests, mountain views and pleasant weather. It is now in Ramban district."
  },
  {
    "id": 68,
    "section": "Udhampur",
    "question": "Where are the Krimchi temples located?",
    "answer": "The Krimchi temples are located in the Krimchi village area of Udhampur district, Jammu and Kashmir."
  },
  {
    "id": 69,
    "section": "Udhampur",
    "question": "Why are the Krimchi temples famous?",
    "answer": "The Krimchi temples are famous for their ancient stone architecture and historical importance. They are among the important heritage sites of the Jammu region."
  },
  {
    "id": 70,
    "section": "Udhampur",
    "question": "What is Ramnagar Fort?",
    "answer": "Ramnagar Fort is a historic fort in Ramnagar town of Udhampur district. It is associated with the region's former rulers and traditional architecture."
  },
  {
    "id": 71,
    "section": "Udhampur",
    "question": "What is the Devika River?",
    "answer": "The Devika River is a sacred river in the Udhampur region. It is respected by local people and is connected with religious traditions."
  },
  {
    "id": 72,
    "section": "Udhampur",
    "question": "What is Kaladi?",
    "answer": "Kaladi is a traditional cheese popular in the Jammu region, especially in Udhampur. It is usually cooked until golden and crisp outside and soft inside."
  },
  {
    "id": 73,
    "section": "Udhampur",
    "question": "Which traditional food is famous in Udhampur?",
    "answer": "Kaladi is one of the most famous traditional foods of Udhampur. Other popular foods include rajma with rice and makki di roti."
  },
  {
    "id": 74,
    "section": "Udhampur",
    "question": "What is Dogri culture?",
    "answer": "Dogri culture is the traditional culture of the Dogra people. It includes the Dogri language, folk songs, dances, festivals, clothing and food."
  },
  {
    "id": 75,
    "section": "Udhampur",
    "question": "What is Mansar Lake?",
    "answer": "Mansar Lake is a beautiful freshwater lake in Jammu and Kashmir. It is surrounded by green hills and is a popular tourist destination in Samba district."
  },
  {
    "id": 76,
    "section": "Udhampur",
    "question": "What is Surinsar Lake?",
    "answer": "Surinsar Lake is a scenic freshwater lake near Jammu city. It is surrounded by hills and greenery and is known for its peaceful atmosphere."
  },
  {
    "id": 77,
    "section": "Udhampur",
    "question": "What natural scenery can be seen around Udhampur?",
    "answer": "The Udhampur region has green hills, forests, valleys, rivers and mountain landscapes. These make it a lovely place for sightseeing and photography."
  },
  {
    "id": 78,
    "section": "Udhampur",
    "question": "What is Chenani famous for?",
    "answer": "Chenani is a town in Udhampur district known for its history and mountain surroundings. It is also associated with the Chenani-Nashri tunnel."
  },
  {
    "id": 79,
    "section": "Udhampur",
    "question": "What is the Dr. Syama Prasad Mookerjee Tunnel?",
    "answer": "It is a major road tunnel in Jammu and Kashmir, formerly known as the Chenani-Nashri Tunnel. It is about 9 kilometres long and helps travellers avoid a difficult mountain road section."
  },
  {
    "id": 80,
    "section": "Udhampur",
    "question": "How can visitors reach Udhampur?",
    "answer": "Visitors can reach Udhampur by road or train. Its railway station connects it with other parts of India."
  },
  {
    "id": 81,
    "section": "Udhampur",
    "question": "What crops are grown in Udhampur?",
    "answer": "Farmers in Udhampur grow crops such as maize, wheat, rice and pulses. Agriculture is an important source of livelihood."
  },
  {
    "id": 82,
    "section": "Udhampur",
    "question": "Which fruits are grown in the region?",
    "answer": "Fruits grown in different parts of the region include apples, walnuts, pears, peaches and plums."
  },
  {
    "id": 83,
    "section": "Udhampur",
    "question": "What is the best time to visit Udhampur?",
    "answer": "Spring and autumn are generally pleasant times to visit Udhampur. Visitors should check the weather and road conditions before travelling."
  },
  {
    "id": 84,
    "section": "Udhampur",
    "question": "Why is Udhampur railway station important?",
    "answer": "Udhampur railway station connects the district with important cities. It supports tourism, trade and passenger travel."
  },
  {
    "id": 85,
    "section": "Udhampur",
    "question": "What traditional clothes are worn in the Jammu region?",
    "answer": "Traditional clothing includes kurtas, salwars, dupattas and other garments worn according to local customs and seasons."
  },
  {
    "id": 86,
    "section": "Udhampur",
    "question": "Which festivals are celebrated in Udhampur?",
    "answer": "People celebrate Lohri, Baisakhi, Diwali, Holi and Navratri. Local fairs and religious celebrations are also important."
  },
  {
    "id": 87,
    "section": "Udhampur",
    "question": "What is Lohri?",
    "answer": "Lohri is a popular winter festival. People gather around bonfires, sing folk songs and share traditional foods such as peanuts and popcorn."
  },
  {
    "id": 88,
    "section": "Udhampur",
    "question": "What is Baisakhi?",
    "answer": "Baisakhi is a harvest festival celebrated in April. It marks the traditional harvest season and is also important to Sikhs."
  },
  {
    "id": 89,
    "section": "Udhampur",
    "question": "Why are local fairs important?",
    "answer": "Local fairs bring people together and help preserve traditional customs, music, crafts and food. They also support local sellers and artists."
  },
  {
    "id": 90,
    "section": "Udhampur",
    "question": "Why are temples important in Udhampur?",
    "answer": "Temples are places of worship, faith and community gatherings. Many temples also have historical and architectural value."
  }
])
QUESTIONS.extend([
    {
        "id": 91,
        "place": "Udhampur",
        "question": "Where is Udhampur located?",
        "answer": "Udhampur is a district in the Union Territory of Jammu and Kashmir in northern India."
    },
    {
        "id": 92,
        "place": "Udhampur",
        "question": "What is the headquarters of Udhampur district?",
        "answer": "Udhampur town is the headquarters of Udhampur district."
    },
    {
        "id": 93,
        "place": "Udhampur",
        "question": "Which language is commonly spoken in Udhampur?",
        "answer": "Dogri is widely spoken in Udhampur, along with Hindi, Urdu and other local languages."
    },
    {
        "id": 94,
        "place": "Udhampur",
        "question": "What is Udhampur famous for?",
        "answer": "Udhampur is known for its beautiful mountains, temples, natural scenery and rich cultural traditions."
    },
    {
        "id": 95,
        "place": "Udhampur",
        "question": "Which famous temple is located in Udhampur?",
        "answer": "The Krimchi temples are among the famous historical temple sites in Udhampur district."
    },
    {
        "id": 96,
        "place": "Udhampur",
        "question": "What is the climate of Udhampur like?",
        "answer": "Udhampur has warm summers, cool winters and pleasant weather in many of its hilly areas."
    },
    {
        "id": 97,
        "place": "Udhampur",
        "question": "What is the main occupation of people in rural Udhampur?",
        "answer": "Agriculture, animal husbandry, small businesses and government services are important occupations."
    },
    {
        "id": 98,
        "place": "Udhampur",
        "question": "Which festival is celebrated with great enthusiasm in Udhampur?",
        "answer": "Festivals such as Baisakhi, Lohri, Diwali and Navratri are celebrated with great enthusiasm."
    },
    {
        "id": 99,
        "place": "Udhampur",
        "question": "What is the traditional language of the region?",
        "answer": "Dogri is an important traditional language of Udhampur and the surrounding Jammu region."
    },
    {
        "id": 100,
        "place": "Udhampur",
        "question": "What kind of natural beauty can be seen in Udhampur?",
        "answer": "Udhampur has green hills, forests, valleys, rivers and beautiful mountain landscapes."
    },
    {
        "id": 101,
        "place": "Udhampur",
        "question": "What is the Krimchi temple group known for?",
        "answer": "The Krimchi temple group is known for its ancient stone temples and historical architecture."
    },
    {
        "id": 102,
        "place": "Udhampur",
        "question": "Why do tourists visit Udhampur?",
        "answer": "Tourists visit Udhampur to enjoy its scenic beauty, religious places, peaceful surroundings and historical sites."
    },
    {
        "id": 103,
        "place": "Udhampur",
        "question": "Which railway station serves Udhampur?",
        "answer": "Udhampur railway station connects the town with other important places through the Indian railway network."
    },
    {
        "id": 104,
        "place": "Udhampur",
        "question": "What is the importance of the Northern Command in Udhampur?",
        "answer": "The Indian Army's Northern Command headquarters is located in Udhampur and plays an important military role."
    },
    {
        "id": 105,
        "place": "Udhampur",
        "question": "Which famous hill destination is near Udhampur?",
        "answer": "Patnitop is a popular hill destination located in the nearby Chenani area."
    },
    {
        "id": 106,
        "place": "Udhampur",
        "question": "What is Patnitop famous for?",
        "answer": "Patnitop is famous for its green meadows, pine forests, mountain views and pleasant weather."
    },
    {
        "id": 107,
        "place": "Udhampur",
        "question": "What is the traditional food of the Jammu region?",
        "answer": "Popular traditional foods include rajma with rice, kaladi, ambal and other Dogra dishes."
    },
    {
        "id": 108,
        "place": "Udhampur",
        "question": "What is kaladi?",
        "answer": "Kaladi is a traditional cheese from the Jammu region, often cooked or fried before serving."
    },
    {
        "id": 109,
        "place": "Udhampur",
        "question": "What is the importance of agriculture in Udhampur?",
        "answer": "Agriculture provides food, employment and income to many families in the rural areas of Udhampur."
    },
    {
        "id": 110,
        "place": "Udhampur",
        "question": "Which crops are grown in Udhampur?",
        "answer": "Farmers grow crops such as maize, wheat, rice and various vegetables depending on the local climate."
    },
    {
        "id": 111,
        "place": "Udhampur",
        "question": "What is the importance of the Chenani-Nashri Tunnel?",
        "answer": "The Chenani-Nashri Tunnel improves road connectivity and reduces travel time between Udhampur and areas towards Ramban."
    },
    {
        "id": 112,
        "place": "Udhampur",
        "question": "What is the official name of the Chenani-Nashri Tunnel?",
        "answer": "The tunnel is officially known as the Dr. Syama Prasad Mookerjee Tunnel."
    },
    {
        "id": 113,
        "place": "Udhampur",
        "question": "What are the major sources of water in Udhampur?",
        "answer": "Rivers, streams, springs, wells and other local water sources provide water to different parts of Udhampur."
    },
    {
        "id": 114,
        "place": "Udhampur",
        "question": "Which river flows through the Udhampur region?",
        "answer": "The Tawi River and its tributaries are important watercourses in the wider Udhampur region."
    },
    {
        "id": 115,
        "place": "Udhampur",
        "question": "Why are forests important in Udhampur?",
        "answer": "Forests help protect wildlife, maintain the environment, prevent soil erosion and support local communities."
    },
    {
        "id": 116,
        "place": "Udhampur",
        "question": "What types of animals are found in the forests around Udhampur?",
        "answer": "The forests of the region support animals such as leopards, monkeys, deer and many kinds of birds."
    },
    {
        "id": 117,
        "place": "Udhampur",
        "question": "How can visitors help keep Udhampur clean?",
        "answer": "Visitors can avoid littering, use dustbins, protect natural areas and respect local communities."
    },
    {
        "id": 118,
        "place": "Udhampur",
        "question": "Why is Udhampur important for transportation?",
        "answer": "Udhampur is an important road and railway link connecting Jammu with several areas of the Chenab Valley."
    },
    {
        "id": 119,
        "place": "Udhampur",
        "question": "What makes Udhampur culturally special?",
        "answer": "Its Dogra traditions, folk music, festivals, local food and historical places make Udhampur culturally special."
    },
    {
        "id": 120,
        "place": "Udhampur",
        "question": "Why should people explore Udhampur?",
        "answer": "People should explore Udhampur to discover its natural beauty, history, culture, traditional food and beautiful surroundings."
    }
])
PAGE = r'''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Explore & Ask</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f3f6ff;
    color: #26334a;
}

header {
    background: linear-gradient(120deg, #4736a5, #168fbd);
    color: white;
    text-align: center;
    padding: 28px 15px;
}

header h1 {
    margin: 0;
    font-size: 34px;
}

header p {
    font-size: 17px;
}

.container {
    max-width: 1000px;
    margin: auto;
    padding: 18px;
}

.controls {
    text-align: center;
    margin: 18px 0;
}

button, select, input {
    padding: 12px;
    margin: 5px;
    border: 0;
    border-radius: 9px;
    font-size: 15px;
}

button {
    background: #5144b8;
    color: white;
    cursor: pointer;
}

button:hover {
    background: #30258a;
}

input {
    width: min(90%, 500px);
    border: 1px solid #aaa;
}

select {
    border: 1px solid #aaa;
}

.section-buttons button {
    background: #e36a38;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    margin: 15px 0;
    box-shadow: 0 3px 12px #00000012;
}

.card h2 {
    color: #4736a5;
}

.answer-image {
    width: 100%;
    max-height: 280px;
    object-fit: cover;
    border-radius: 12px;
    margin-top: 10px;
}

.question-button {
    display: block;
    width: 100%;
    text-align: left;
    background: #edf0ff;
    color: #26334a;
    margin: 7px 0;
}

.question-button:hover {
    background: #d9e0ff;
}

#answer {
    line-height: 1.7;
    font-size: 17px;
}

#counter {
    font-weight: bold;
    color: #4736a5;
}

footer {
    text-align: center;
    padding: 20px;
    color: #666;
}
</style>
</head>

<body>

<header>
    <h1>🌏 Explore & Ask</h1>
    <p>Discover Japan and Udhampur through questions!</p>
</header>

<div class="container">

    <div class="controls">
        <button onclick="setPlace('Japan')">🇯🇵 Japan</button>
        <button onclick="setPlace('Udhampur')">🏔️ Udhampur</button>
        <button onclick="setPlace('All')">🌍 All Questions</button>
        <br>
        <button onclick="setLanguage('en')">English</button>
        <button onclick="setLanguage('hi')">हिन्दी</button>
    </div>

    <div class="card">
        <h2 id="welcome">Welcome to Explore & Ask!</h2>
        <p id="description">Choose a place or search for a question.</p>

        <input
            id="search"
            type="text"
            placeholder="Search for a question..."
            oninput="showQuestions()"
        >

        <p id="counter">Questions explored: 0</p>
    </div>

    <div class="card">
        <h2 id="listTitle">Browse Questions</h2>
        <div id="questionList"></div>
    </div>

    <div class="card" id="answerCard" style="display:none;">
        <h2 id="question"></h2>
        <p id="answer"></p>
        <img id="answerImage" class="answer-image" alt="Place picture">

        <div class="controls">
            <button onclick="speakAnswer()">🔊 Speak Answer</button>
            <button onclick="speakAnswer()">🔁 Repeat Answer</button>
            <button onclick="stopSpeaking()">⏹ Stop Speaking</button>
            <button onclick="anotherQuestion()">Another Question</button>
        </div>
    </div>

</div>

<footer>
    Explore & Ask | Learn something new every day!
</footer>

<script>
let allQuestions = [];
let currentPlace = "All";
let language = "en";
let explored = new Set();

const translations = {
    en: {
        welcome: "Welcome to Explore & Ask!",
        description: "Choose a place or search for a question.",
        list: "Browse Questions",
        search: "Search for a question...",
        counter: "Questions explored: ",
        unavailable: "Sorry, no matching question was found.",
        empty: "Please choose a question."
    },
    hi: {
        welcome: "Explore & Ask में आपका स्वागत है!",
        description: "कोई स्थान चुनें या प्रश्न खोजें।",
        list: "सभी प्रश्न देखें",
        search: "अपना प्रश्न खोजें...",
        counter: "देखे गए प्रश्न: ",
        unavailable: "क्षमा करें, इस प्रश्न का उत्तर नहीं मिला।",
        empty: "कृपया एक प्रश्न चुनें।"
    }
};

const pictures = {
    Japan: [
        "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=900",
        "https://images.unsplash.com/photo-1490806843957-31f4c9a91c65?w=900"
    ],
    Udhampur: [
        "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=900",
        "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=900"
    ]
};

function updateLabels() {
    const t = translations[language];
    document.getElementById("welcome").textContent = t.welcome;
    document.getElementById("description").textContent = t.description;
    document.getElementById("listTitle").textContent = t.list;
    document.getElementById("search").placeholder = t.search;
    updateCounter();
}

function updateCounter() {
    document.getElementById("counter").textContent =
        translations[language].counter + explored.size;
}

function setLanguage(lang) {
    language = lang;
    updateLabels();
    showQuestions();
}

function setPlace(place) {
    currentPlace = place;
    document.getElementById("search").value = "";
    document.getElementById("answerCard").style.display = "none";
    showQuestions();
}

function showQuestions() {
    const list = document.getElementById("questionList");
    const search = document.getElementById("search").value.toLowerCase();

    list.innerHTML = "";

    const filtered = allQuestions.filter(q => {
        const matchesPlace =
            currentPlace === "All" || q.place === currentPlace;

        const matchesSearch =
            q.question.toLowerCase().includes(search);

        return matchesPlace && matchesSearch;
    });

    if (filtered.length === 0) {
        list.textContent = translations[language].unavailable;
        return;
    }

    filtered.forEach(q => {
        const button = document.createElement("button");
        button.className = "question-button";
        button.textContent = q.id + ". " + q.question;
        button.onclick = () => showAnswer(q);
        list.appendChild(button);
    });
}

function showAnswer(q) {
    document.getElementById("answerCard").style.display = "block";
    document.getElementById("question").textContent = q.question;
    document.getElementById("answer").textContent = q.answer;

    const images = pictures[q.place];
    const image = document.getElementById("answerImage");
    image.src = images[q.id % images.length];

    explored.add(q.id);
    updateCounter();

    window.scrollTo({
        top: document.getElementById("answerCard").offsetTop,
        behavior: "smooth"
    });
}

function anotherQuestion() {
    const available = allQuestions.filter(q =>
        currentPlace === "All" || q.place === currentPlace
    );

    if (available.length === 0) {
        alert(translations[language].empty);
        return;
    }

    const question = available[
        Math.floor(Math.random() * available.length)
    ];

    showAnswer(question);
}

function speakAnswer() {
    if (!("speechSynthesis" in window)) {
        alert("Speech is not supported in this browser.");
        return;
    }

    stopSpeaking();

    const text = document.getElementById("answer").textContent;
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = language === "hi" ? "hi-IN" : "en-IN";
    window.speechSynthesis.speak(speech);
}

function stopSpeaking() {
    if ("speechSynthesis" in window) {
        window.speechSynthesis.cancel();
    }
}

fetch("/api/questions")
    .then(response => response.json())
    .then(data => {
        allQuestions = data;
        showQuestions();
    })
    .catch(() => {
        document.getElementById("questionList").textContent =
            "Questions could not be loaded. Please restart the website.";
    });

updateLabels();
</script>

</body>
</html>
'''
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/api/questions":
            data = json.dumps(
                QUESTIONS,
                ensure_ascii=False
            ).encode("utf-8")

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )
            self.send_header(
                "Content-Length",
                str(len(data))
            )
            self.end_headers()
            self.wfile.write(data)

        elif self.path == "/health":
            data = b"OK"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        else:
            data = PAGE.encode("utf-8")

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "text/html; charset=utf-8"
            )
            self.send_header(
                "Content-Length",
                str(len(data))
            )
            self.end_headers()
            self.wfile.write(data)


def main():
    server = ThreadingHTTPServer(
        ("0.0.0.0", PORT),
        Handler
    )

    print("Explore & Ask website is running!")
    print("Open this address in your browser:")
    print("http://127.0.0.1:" + str(PORT))

    server.serve_forever()


if __name__ == "__main__":
    main()
