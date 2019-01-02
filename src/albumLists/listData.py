import logging

def getAlbumListData():

	list2018 = list()

	list2018.append(Album("Idles","Joy as an Act of Resistance","https://ia802900.us.archive.org/31/items/mbid-882917bf-09f9-42c2-8c3e-41bb741d126e/mbid-882917bf-09f9-42c2-8c3e-41bb741d126e-21045674015_thumb500.jpg","https://open.spotify.com/album/7BbRSUBwTB37ut0Ht3yAqt?si=gBMI7wTASSSTrPsUf0FNOg"))
	list2018.append(Album("Daughters","You Won't Get What You Want","https://ia800701.us.archive.org/20/items/mbid-8d3cddb8-3cd5-4e03-8c2d-cfe1aa8447d7/mbid-8d3cddb8-3cd5-4e03-8c2d-cfe1aa8447d7-21381925212_thumb500.jpg","https://open.spotify.com/album/7w7ZTlk8YLc0OxviTp97qA?si=xDfnG9YoSRqntMmlFKDb4g"))
	list2018.append(Album("Parquet Courts","Wide Awake!","https://ia802801.us.archive.org/9/items/mbid-b429fde4-8676-4af6-9478-0b3bb172ac8a/mbid-b429fde4-8676-4af6-9478-0b3bb172ac8a-19913288269_thumb500.jpg","https://open.spotify.com/album/5uTI2HcpAywDP8Vo1DpJta?si=wEse6IFITsGVwL1INp50yQ"))
	list2018.append(Album("A.A.L. (Against All Logic)","2012-2017","https://ia802804.us.archive.org/19/items/mbid-395900a3-318d-46d2-8358-947a6f2ea910/mbid-395900a3-318d-46d2-8358-947a6f2ea910-19463819571_thumb500.jpg","https://open.spotify.com/album/1uzfGk9vxMXfaZ2avqwxod?si=ReyQbPRxSXmI531QCKTILw"))
	list2018.append(Album("Shame","Songs of Praise","https://ia902803.us.archive.org/7/items/mbid-f2b0e0b1-ae55-461d-aa8e-db893f3047f1/mbid-f2b0e0b1-ae55-461d-aa8e-db893f3047f1-20576668677_thumb500.jpg","https://open.spotify.com/album/3A1kutvBmC6czSsSv7aR5E?si=Z1mD27UtSvOSU4_YFEy3Xw"))

	list2018.append(Album("Deafheaven","Ordinary Corrupt Human Love","https://ia802903.us.archive.org/20/items/mbid-d1aa5869-a1f8-4646-afc2-abfe3fdd4368/mbid-d1aa5869-a1f8-4646-afc2-abfe3fdd4368-20532633765_thumb500.jpg","https://open.spotify.com/album/2iA7rzpQsOfAPkfH4Ekp7f?si=QuQgRCsGQLyZPubeORyUhA"))
	list2018.append(Album("Snail Mail","Lush","https://coverartarchive.org/release/05ea6699-1c57-49b7-a6f7-bb361982f4d7/19420888579_thumb500.jpg","https://open.spotify.com/album/2e48GqjEwCi87gQJanb1bf?si=yNd_Kz9rSQ6Cx8QaAdrgIA"))
	list2018.append(Album("The Beths","Future Me Hates Me","https://ia802900.us.archive.org/23/items/mbid-018c2a22-52d6-4cda-a489-9b19ead0dd85/mbid-018c2a22-52d6-4cda-a489-9b19ead0dd85-20631718109_thumb500.jpg","https://open.spotify.com/album/4xG41eVnTuDK6uMmcksQ9B?si=e9vF2wtoTsWa1AwDSA9nlg"))
	list2018.append(Album("Beach House","7","https://ia802804.us.archive.org/28/items/mbid-2ed28366-d982-4671-aec0-632cda8ca9bb/mbid-2ed28366-d982-4671-aec0-632cda8ca9bb-19290765672_thumb500.jpg","https://open.spotify.com/album/4qftBBO7pnYlek3mRENIvM?si=Bwjs00hnRwmmSXoVxgHLNA"))
	list2018.append(Album("Nils Frahm","All Melody","https://ia800107.us.archive.org/12/items/mbid-7ebabd10-6943-494b-bbb9-8c38d164f342/mbid-7ebabd10-6943-494b-bbb9-8c38d164f342-18822492433_thumb500.jpg","https://open.spotify.com/album/3MH77JVM17CEdDLz374t1e?si=6SX3MIAJQkW8rdzNYaHh6Q"))

	list2018.append(Album("Jon Hopkins","Singularity","https://ia802800.us.archive.org/26/items/mbid-30161b32-5bf3-4ea5-8a13-4dbddfb40699/mbid-30161b32-5bf3-4ea5-8a13-4dbddfb40699-19771732225_thumb500.jpg","https://open.spotify.com/album/1nvzBC1M3dlCMIxfUCBhlO?si=MzjC1r6URY25AjI4hOWYhA"))
	list2018.append(Album("Earl Sweatshirt","Some Rap Songs","https://ia601503.us.archive.org/8/items/mbid-bb12aa9f-824c-4c3d-8e6c-5cb1f40b3ca3/mbid-bb12aa9f-824c-4c3d-8e6c-5cb1f40b3ca3-21597302452_thumb500.jpg","https://open.spotify.com/album/66at85wgO2pu5CccvqUF6i?si=qOyq22WiRkmcDuRYmmM25g"))	
	list2018.append(Album("Caroline Rose","Loner","https://ia802806.us.archive.org/6/items/mbid-ed177cdd-f5d5-481f-b0fe-b76d353f4fcb/mbid-ed177cdd-f5d5-481f-b0fe-b76d353f4fcb-19293291137_thumb500.jpg","https://open.spotify.com/album/2ztVsnlMAsHqVe1BjoICnr?si=lFyAc4OwSimADS559eYyaQ"))
	list2018.append(Album("Flasher","Constant Image","https://ia802804.us.archive.org/25/items/mbid-ad6b9da1-7ae8-4fde-b4f2-5ef912817f68/mbid-ad6b9da1-7ae8-4fde-b4f2-5ef912817f68-19938930527_thumb500.jpg","https://open.spotify.com/album/6fvUDhvz6hDVck9epHLnf6?si=CpkvGoIlSxuraOXMG9qPmw"))
	list2018.append(Album("Tim Hecker","Konoyo","https://ia802901.us.archive.org/3/items/mbid-359c37a9-bd1e-48db-b892-6f96846403e4/mbid-359c37a9-bd1e-48db-b892-6f96846403e4-21105151709_thumb500.jpg","https://open.spotify.com/album/4TU8d9DGafZZiyN7peC4sl?si=MABbS-UDR_SDCWecG4DsvQ"))

	list2018.append(Album("Holy Fawn","Death Spells","https://ia800700.us.archive.org/10/items/mbid-2fecd74f-e921-4ed1-b5bb-23dccb6e9203/mbid-2fecd74f-e921-4ed1-b5bb-23dccb6e9203-20973015984_thumb500.jpg","https://open.spotify.com/album/7FftBO1RPryPqS91iua3ne?si=JgbnaT_jQfuZ16C8VLYY7w"))
	list2018.append(Album("Young Fathers","Cocoa Sugar","https://ia902802.us.archive.org/0/items/mbid-11ce37ca-3894-4269-a609-5bb916bfcedf/mbid-11ce37ca-3894-4269-a609-5bb916bfcedf-19763834370_thumb500.jpg","https://open.spotify.com/album/03Dp6OJS4wd7dI1rRszPwj?si=AuAr0U7uTTCYJIOSWqc0UQ"))
	list2018.append(Album("Let's Eat Grandma","I'm All Ears","https://ia902809.us.archive.org/2/items/mbid-139863bd-b500-4a08-84c5-d05c10e08575/mbid-139863bd-b500-4a08-84c5-d05c10e08575-20311150673_thumb500.jpg","https://open.spotify.com/album/5Bnhkya5cGltQFTrnC0grx?si=CKk8lqiqRnGnrGbIUjU0zQ"))
	list2018.append(Album("Neko Case","Hell-On","https://ia802803.us.archive.org/17/items/mbid-e7a7a58c-2dbc-485c-9a75-54ba41defda6/mbid-e7a7a58c-2dbc-485c-9a75-54ba41defda6-20060472950_thumb500.jpg","https://open.spotify.com/album/7I141P48NQw206up7jBezG?si=pevqfJSsQpumFpK6VEeoKw"))
	list2018.append(Album("Iceage","Beyondless","https://ia902808.us.archive.org/1/items/mbid-d1b776d6-d7c7-4505-b6df-0e7bfba0c2db/mbid-d1b776d6-d7c7-4505-b6df-0e7bfba0c2db-20357897053_thumb500.jpg","https://open.spotify.com/album/5H8wFFblf7YvGc7LbBzuR9?si=9S52EbEwQMiPavMQYIk0aQ"))

	list2018.append(Album("Car Seat Headrest","Twin Fantasy","https://ia802804.us.archive.org/10/items/mbid-66d6168d-14f2-48bf-8c5f-a125401ebaa7/mbid-66d6168d-14f2-48bf-8c5f-a125401ebaa7-19013827522_thumb500.jpg","https://open.spotify.com/album/20U1UWeGcGq7JVW0tf8yfH?si=BCk-UUV-R3qVo71wYmWNJA"))
	list2018.append(Album("Chastity","Death Lust","https://f4.bcbits.com/img/a2897047827_10.jpg","https://open.spotify.com/album/57j0H5oZv58jTE1kR4kjIg?si=LSqRpaTNSzmFL_JGNyWt4g"))
	list2018.append(Album("Adrianne Lenker","abysskiss","https://f4.bcbits.com/img/a2245808128_10.jpg","https://open.spotify.com/album/5W6TxvIqACEfnxm0VgPhv7?si=R5L8iaXgQhKd5pDe9fpV9A"))	
	list2018.append(Album("Tropical Fuck Storm","A Laughing Death in Meatspace","https://ia802806.us.archive.org/6/items/mbid-5ad30adb-4ed8-4ead-a404-e780de1cc45d/mbid-5ad30adb-4ed8-4ead-a404-e780de1cc45d-19863197935_thumb500.jpg","https://open.spotify.com/album/1Q351pwqlWprsmF8fIudo6?si=CUQctXbzTmKQuAzRvPxOPg"))
	list2018.append(Album("Hop Along","Bark Your Head Off, Dog","https://ia800108.us.archive.org/25/items/mbid-e5b2ec24-8d2c-4641-8058-815cb35e67a7/mbid-e5b2ec24-8d2c-4641-8058-815cb35e67a7-18918680426_thumb500.jpg","https://open.spotify.com/album/7taAuoHvZ4LJzEaB0OzuP3?si=eEwiy_XBRp-AOr6u8w1u-g"))

	list2018.append(Album("boygenius","boygenius","https://ia802907.us.archive.org/26/items/mbid-3fa9804c-3721-406c-b176-83f768389c30/mbid-3fa9804c-3721-406c-b176-83f768389c30-21304666857_thumb500.jpg","https://open.spotify.com/album/5BRORKnC2HD5xhgUyR31SH?si=yOx2v8XlTD6LxfsS2YRKWQ"))
	list2018.append(Album("Mikaela Davis","Delivery","https://ia601508.us.archive.org/14/items/mbid-c356329a-7052-4292-b0a0-66f467ef072c/mbid-c356329a-7052-4292-b0a0-66f467ef072c-21696383895_thumb500.jpg","https://open.spotify.com/album/4FUgK5s0hDVf5yKIOwq7ex?si=3VK5BiLnRW-s26xC3oCpGQ"))
	list2018.append(Album("Sons of Kemet","Your Queen is a Reptile","https://ia902803.us.archive.org/10/items/mbid-7ac02e18-decf-4003-8b79-c035ae1a8fb8/mbid-7ac02e18-decf-4003-8b79-c035ae1a8fb8-19544207848_thumb500.jpg","https://open.spotify.com/album/4pxnDGBdoGu88h8ZInX5f5?si=WCnsV3NlQgOrEFElEb5Djw"))
	list2018.append(Album("HOLY","All These Worlds are Yours","https://ia600108.us.archive.org/2/items/mbid-8a7f2759-e1ec-4e23-bf91-42e501065dae/mbid-8a7f2759-e1ec-4e23-bf91-42e501065dae-18971228148_thumb500.jpg","https://open.spotify.com/album/2xD41zvm7Mn7mB64IWtUHs?si=1y6OO7P_Rjmqb3ZNdH4xBA"))
	list2018.append(Album("Sloucher","Be True","https://f4.bcbits.com/img/a3625052353_10.jpg","https://open.spotify.com/album/0ozxvtCkDsMFNvvSPeZAWm?si=E9S7frHSR_a2pddDqlO-rw"))

	runnersUp2018 = list()

	runnersUp2018.append(Album("Bodega","Endless Scroll","https://f4.bcbits.com/img/a1596674546_10.jpg","https://open.spotify.com/album/2L8xdzyyH71fza7w3OILzl?si=qwV4hbp4TOyxo4NkCA6lXA"))
	runnersUp2018.append(Album("Jean Grae x Quelle Chris","Everything's Fine","https://ia800107.us.archive.org/33/items/mbid-ea68a4bc-23fa-4098-bdc4-b2f945ae1b61/mbid-ea68a4bc-23fa-4098-bdc4-b2f945ae1b61-18919779443_thumb500.jpg","https://open.spotify.com/album/22oHrB4SLwayyuLE02t5BD?si=kusCSwHpSpKrURNmyNOlww"))
	runnersUp2018.append(Album("Kathryn Joseph","From When I Wake the Want Is","https://ia601508.us.archive.org/5/items/mbid-f8664fed-1eba-4a2e-ab66-5df4fe45cf39/mbid-f8664fed-1eba-4a2e-ab66-5df4fe45cf39-21798623072_thumb500.jpg","https://open.spotify.com/album/7faUUBGOjjw16j2GGgSsS3?si=-jFNETjKROCyo3q915XP3A"))
	runnersUp2018.append(Album("Moses Sumney","Black in Deep Red, 2014","https://f4.bcbits.com/img/a1292895729_10.jpg","https://open.spotify.com/album/7q1a6OEw4MtYUIzG5SFOi3?si=zJmHUmX-Q5afH-bfz-X-zw"))
	runnersUp2018.append(Album("Jeff Tweedy","WARM","https://ia902901.us.archive.org/34/items/mbid-b9fe982a-3ddb-490f-b702-18b26e66b929/mbid-b9fe982a-3ddb-490f-b702-18b26e66b929-21759024089_thumb500.jpg","https://open.spotify.com/album/2XTPulCL6EUx1thyJPnlmj?si=LCEjgRyjRfudlhEfjAfqCw"))
	

	spreadsheet2018 = dict()
	spreadsheet2018["link"] = "https://docs.google.com/spreadsheets/d/1TwqYRoASC53dyPAufxxoMBPv4efacT3zJ9aZrQxBV-g/edit#gid=0"
	spreadsheet2018["ratingCount"] = "536"
	spreadsheet2018["averageRating"] = "6.36"

	albums2018 = dict()
	albums2018["list"] = list2018
	albums2018["runnersUp"] = runnersUp2018
	albums2018["spreadsheet"] = spreadsheet2018


	list2017 = list()

	list2017.append(Album("Big Thief","Capacity","https://coverartarchive.org/release-group/3fd9b616-15ec-4a3d-81df-866bd9942202/front.jpg",""))
	list2017.append(Album("Protomartyr","Relatives in Descent","https://coverartarchive.org/release/4734f1c1-6529-41ac-9c88-5ff82cb6e13c/18324922657.jpg",""))
	list2017.append(Album("Idles","Brutalism","https://coverartarchive.org/release/6d4e53b2-82d1-4154-907d-00f243284f2b/16733187540.jpg",""))
	list2017.append(Album("Gang of Youths","Go Farther in Lightness","https://ia800809.us.archive.org/8/items/mbid-05a13538-a9c8-45cc-87b1-6fe51bce08f7/mbid-05a13538-a9c8-45cc-87b1-6fe51bce08f7-20244359129_thumb500.jpg",""))
	list2017.append(Album("Priests","Nothing Feels Natural","https://coverartarchive.org/release/003c411f-e563-461b-963b-f3ec51498975/15687611371.jpg",""))

	list2017.append(Album("Manchester Orchestra","A Black Mile to the Surface","https://coverartarchive.org/release-group/0e044656-b567-473e-ad96-bec356ce2aba/front.jpg",""))
	list2017.append(Album("Jesca Hoop","Memories are Now","https://coverartarchive.org/release-group/0f843344-01b0-4b18-a7f6-568f2f0b0d57/front.jpg",""))
	list2017.append(Album("Slowdive","Slowdive","https://coverartarchive.org/release-group/9318347d-b4bc-4b50-bd5e-c9a9fcb9aa98/front.jpg",""))
	list2017.append(Album("Fleet Foxes","Crack-Up","https://coverartarchive.org/release-group/0a35f45c-c89c-418a-93e5-e29ed1d34caf/front.jpg",""))
	list2017.append(Album("Elder","Reflections of a Floating World","https://coverartarchive.org/release-group/474f819f-def3-49c8-b764-381649d9e8c3/front.png",""))

	list2017.append(Album("Broken Social Scene","Hug of Thunder","https://coverartarchive.org/release-group/02c033c9-f660-48cb-9927-531a02a6bd9a/front.jpg",""))
	list2017.append(Album("Pile","A Hairshirt of Purpose","https://coverartarchive.org/release/5b32481d-d434-4841-97bf-84802472135d/16362889103.jpg",""))
	list2017.append(Album("The National","Sleep Well Beast","https://coverartarchive.org/release/60a2da10-a7bc-43a1-8e36-eeffc624034d/16694939757.jpg",""))
	list2017.append(Album("Kendrick Lamar","DAMN.","https://coverartarchive.org/release-group/b88655ba-7469-48b8-a296-b9011ab73ef3/front.jpg",""))
	list2017.append(Album("Julien Baker","Turn Out the Lights","https://coverartarchive.org/release-group/5768576a-679d-4ae4-a04d-e41da4998aa1/front.jpg",""))

	list2017.append(Album("All Them Witches","Sleeping Through the War","https://coverartarchive.org/release-group/d83178d3-82da-460d-a7b7-481212c50407/front.png",""))
	list2017.append(Album("Converge","The Dusk in Us","https://coverartarchive.org/release-group/fe96f1f4-5c9f-4a39-a9d1-181dd3f4c54b/front.jpg",""))
	list2017.append(Album("Rolling Blackouts Coastal Fever","The French Press","https://coverartarchive.org/release-group/aa1eb1e1-4f46-43c2-83d6-94ca9e20a9de/front.jpg",""))
	list2017.append(Album("Blanck Mass","World Eater","https://coverartarchive.org/release-group/4b0b8787-57c2-4374-9d5d-63a9e4440dff/front.jpg",""))
	list2017.append(Album("Wolf Alice","Visions of a Life","https://coverartarchive.org/release-group/7f231c61-20b2-49d6-ac66-1cacc4cc775f/front.png",""))

	list2017.append(Album("Waxahatchee","Out in the Storm","https://coverartarchive.org/release-group/b3808167-f635-4e88-b0c4-a7873e86237e/front.jpg",""))
	list2017.append(Album("Caddywhompus","Odd Hours","https://coverartarchive.org/release-group/779b0f7e-c925-4240-9fd6-d2aa20b8c051/front.jpg",""))
	list2017.append(Album("Julie Byrne","Not Even Happiness","https://coverartarchive.org/release-group/5bb8e065-25f9-4427-85a6-56979cb99b19/front.jpg",""))
	list2017.append(Album("Charlotte Gainsbourg","Rest","https://coverartarchive.org/release-group/78ccbb45-a0d2-47f0-b43e-0716831c7864/front.jpg",""))
	list2017.append(Album("Sorority Noise","You're not as ____ as you Think","https://coverartarchive.org/release-group/625ae1df-cb44-40fa-bc56-46eda0c9ce8b/front.jpg",""))

	list2017.append(Album("Do Make Say Think","Stubborn Persistent Illusions","https://coverartarchive.org/release-group/d17b9d5a-3a89-4650-94a3-81ca88375828/front.jpg",""))
	list2017.append(Album("Grandbrothers","Open","https://coverartarchive.org/release-group/66610789-fd17-404b-b894-2272012ca046/front.jpg",""))
	list2017.append(Album("Billy Woods","Known Unknowns","https://coverartarchive.org/release-group/7f3f840b-8ca2-4d7b-a52b-daf45708eb62/front.jpg",""))
	list2017.append(Album("Quicksand","Interiors","https://coverartarchive.org/release-group/985de8de-1a8b-4ee5-91ce-a1e6aefad108/front.jpg",""))
	list2017.append(Album("Alvvays","Antisocialites","https://coverartarchive.org/release-group/1f0a3090-ae8c-4fbd-9b70-b4371961ef11/front.jpg",""))

	runnersUp2017 = list()

	runnersUp2017.append(Album("Alex Cameron","Forced Witness","https://coverartarchive.org/release-group/43f7ce86-9448-4914-a867-5220b4a7555d/front.jpg",""))
	runnersUp2017.append(Album("Ibeyi","Ash","https://coverartarchive.org/release-group/19f89c3e-3802-423e-b155-7e39104abff7/front.jpg",""))
	runnersUp2017.append(Album("Photay","Onism","https://coverartarchive.org/release-group/8063670b-1bd7-4ef8-a239-b5c80548462d/front.jpg",""))
	runnersUp2017.append(Album("Thunder Dreamer","Capture","https://f4.bcbits.com/img/a1250759136_10.jpg",""))
	runnersUp2017.append(Album("Young Jesus","S/T","http://giganticnoise.com/wp-content/uploads/2017/07/Young-Jesus-Front-Cover.jpg",""))

	spreadsheet2017 = dict()
	spreadsheet2017["link"] = "https://docs.google.com/spreadsheets/d/1TwqYRoASC53dyPAufxxoMBPv4efacT3zJ9aZrQxBV-g/edit#gid=0"
	spreadsheet2017["ratingCount"] = "518"
	spreadsheet2017["averageRating"] = "6.36"

	albums2017 = dict()
	albums2017["list"] = list2017
	albums2017["runnersUp"] = runnersUp2017
	albums2017["spreadsheet"] = spreadsheet2017



	list2016 = list()
	list2016.append(Album("Pinegrove","Cardinal","https://coverartarchive.org/release/470f6a84-5d38-4544-8130-aa80b67c4fe7/12958866716.jpg", "https://open.spotify.com/album/2SmrUzUMMOYQqoPuOhlhjw"))
	list2016.append(Album("Car Seat Headrest","Teens of Denial","https://coverartarchive.org/release-group/7413db7e-163c-4e48-bd8e-c41fd466b2c1/front.jpg", "https://open.spotify.com/album/26DseQO366JfXwIP7dIgQj"))
	list2016.append(Album("Radiohead","A Moon Shaped Pool","https://coverartarchive.org/release/0c46011c-2c86-4c53-8226-10c79f746e6f/13889765748.jpg", "https://open.spotify.com/album/6vuykQgDLUCiZ7YggIpLM9"))
	list2016.append(Album("Angel Olsen","My Woman","https://coverartarchive.org/release-group/c9db1003-a83a-49b7-b04c-237e05260969/front.jpg", "https://open.spotify.com/album/5M8xQaQZuW2LZGVXZ3mlKN"))
	list2016.append(Album("Michael Kiwanuka","Love & Hate","https://coverartarchive.org/release-group/c51bb243-59ac-4de0-9a51-4ead3d4e1bf8/front.jpg", "https://open.spotify.com/album/0qxsfpy2VU0i4eDR9RTaAU"))

	list2016.append(Album("Anderson .Paak","Malibu","https://coverartarchive.org/release/844eb096-2b84-4c8f-9922-7f287126b39e/12723136519.jpg", "https://open.spotify.com/album/4VFG1DOuTeDMBjBLZT7hCK"))
	list2016.append(Album("Nicolas Jaar","Sirens","https://coverartarchive.org/release-group/9ce4d1c9-31d4-410b-98cf-207b85086e89/front.jpg", "https://open.spotify.com/album/2EvZiOMBlC9b5hbjbZCjZv"))
	list2016.append(Album("Whitney","Light Upon the Lake","https://coverartarchive.org/release-group/6f6b2682-b458-4560-9fa9-73a6b6302e32/front.jpg", "https://open.spotify.com/album/5yMCA6HdFAeL1aqUjxO3MO"))
	list2016.append(Album("A Tribe Called Quest","We Got it from Here... Thank You 4 Your Service","https://coverartarchive.org/release-group/b445860f-edd9-4160-841c-fccf5533ecbd/front.jpg", "https://open.spotify.com/album/3WvQpufOsPzkZvcSuynCf3"))
	list2016.append(Album("MONEY","Suicide Songs","https://coverartarchive.org/release-group/0c192e53-6b2c-4ece-bea5-624a44f40274/front.jpg", "https://open.spotify.com/album/4Yrey9xf8CYNrKaeSgTGAs"))

	list2016.append(Album("Slow Dakota","The Ascension of Slow Dakota","https://f4.bcbits.com/img/a2211100948_10.jpg", "https://open.spotify.com/album/4h7NRdxlDtkLPlQssE6O10"))
	list2016.append(Album("Explosions in the Sky","The Wilderness","https://coverartarchive.org/release/f8068355-0dce-4845-88ca-1330764db570/13191737587.png", "https://open.spotify.com/album/79X3DX8IqI3jZXQvsrFiDV"))
	list2016.append(Album("Bon Iver","22, A Million","https://coverartarchive.org/release-group/f0e8f425-a941-48df-b5d7-2ceeaaf77c71/front.jpg", "https://open.spotify.com/album/1PgfRdl3lPyACfUGH4pquG"))
	list2016.append(Album("Parquet Courts","Human Performance","https://coverartarchive.org/release-group/3353a8a0-a5ab-4970-b34e-090afcc2bba7/front.jpg", "https://open.spotify.com/album/4RNew41ZeRuoRNg3YAhvpe"))
	list2016.append(Album("Yak","Alas Salvation","https://coverartarchive.org/release-group/3e71c910-8365-400f-be1c-6d2e85575c6d/front.jpg", "https://open.spotify.com/album/79eEK4Zv0dqVXrarAmqozS"))

	list2016.append(Album("Greys","Outer Heaven","https://coverartarchive.org/release-group/205f7615-fb62-4e4d-9e3a-f26198c4c679/front.png", "https://open.spotify.com/album/0wB19rOCyof5vPv6pYnCDH"))
	list2016.append(Album("The Drones","Feelin Kinda Free","https://coverartarchive.org/release-group/2636b2df-f2b7-48dd-866a-09c0e6c54b64/front.jpg", "https://open.spotify.com/album/4qv5FxVbJgGyHJZKt2u0qv"))
	list2016.append(Album("Swans","The Glowing Man","https://coverartarchive.org/release/4c9dbfae-4744-4379-b9ad-de28670c944a/13234260103.jpg", "https://open.spotify.com/album/6kYSd8r3ef5bssfOO58PX4"))
	list2016.append(Album("The Avalanches","Wildflower","https://coverartarchive.org/release-group/e27e2c64-8e49-43d2-8468-c3b484cf11f0/front.jpg", "https://open.spotify.com/album/0j0djiGxLnBiW7meVc2PER"))
	list2016.append(Album("Hamilton Leithauser + Rostam","I Had a Dream That You Were Mine","https://coverartarchive.org/release/059ad661-7be2-4ba9-b495-32254ef4887a/14709768096.jpg", "https://open.spotify.com/album/2TDuXjtpO4tdvm86KVNMk0"))

	list2016.append(Album("Big Thief","Masterpiece","https://coverartarchive.org/release-group/134104b9-926e-40fc-a975-e6a0f3b238d5/front.jpg", "https://open.spotify.com/album/4onPyHor2yOlVxCsIaGyHH"))
	list2016.append(Album("Japanese Breakfast","Psychopomp","https://coverartarchive.org/release-group/ac6989e6-0589-41e9-b03c-1c4cb80a27d6/front.jpg", "https://open.spotify.com/album/3i7EHinpu9J5MXKMzjpjZ0"))
	list2016.append(Album("John K. Samson","Winter Wheat","https://coverartarchive.org/release/a734090d-0f2b-4cda-bd5f-b3fad7a932ae/15196950742.jpg", "https://open.spotify.com/album/28vCM0a4MYPwcTervwP7Ia"))
	list2016.append(Album("Preoccupations","Preoccupations","https://coverartarchive.org/release/d2a9d069-efd0-4a57-93e0-a43f5299817f/14092596668.jpg", "https://open.spotify.com/album/1BedrXdH4el7fWWIYMC99N"))
	list2016.append(Album("The Hotelier","Goodness","https://coverartarchive.org/release/88eb2526-e91f-4405-b6d8-eeef3b3cd8cd/13667263818.jpg", "https://open.spotify.com/album/5SYW9HBk4WxetFTcbcK3nk"))

	list2016.append(Album("Chris Staples","Golden Age","https://images-na.ssl-images-amazon.com/images/I/61FZkJnTRIL.jpg", "https://open.spotify.com/album/3kcttgC0Cwuc1ZXqYaIGmM"))
	list2016.append(Album("PUP","The Dream is Over","https://coverartarchive.org/release-group/98b0184a-c19c-4a21-917f-b09907eccf85/front.jpg", "https://open.spotify.com/album/7lelUe4aaCQmOMJKsQvirf"))
	list2016.append(Album("Weaves","Weaves","https://coverartarchive.org/release-group/a39ef3dd-77a6-47c3-ad56-f6bbc998aaf5/front.jpg", "https://open.spotify.com/album/3KyE0xdGrp9Sl9xErn7Zcd"))
	list2016.append(Album("Danny Brown","Atrocity Exhibition","https://coverartarchive.org/release-group/88f4f8e5-ee88-4050-84ad-cf73f7c2b19a/front.jpg", "https://open.spotify.com/album/3e7vtKJ3m1zVh38VGq2g3H"))
	list2016.append(Album("Nick Cave and the Bad Seeds","Skeleton Tree","https://coverartarchive.org/release-group/49339024-c6b4-4345-b521-6349463513cb/front.jpg", "https://open.spotify.com/album/34xaLN7rDecGEK5UGIVbeJ"))

	runnersUp2016 = list()

	runnersUp2016.append(Album("Holy Esque","At Hope's Ravine","https://coverartarchive.org/release-group/a53ab4fc-1d0d-4092-b4f6-5420de0ba8c5/front.jpg", "https://open.spotify.com/album/3zBzH0JnOdII8wGZU0SjDR"))
	runnersUp2016.append(Album("Mothers","When You Walk a Long Distance you are Tired","https://coverartarchive.org/release-group/1aca6863-4dda-4a6e-8818-e1bc8c756373/front.jpg", "https://open.spotify.com/album/6T0QEKUvqfDxyVJIUZTkYe"))
	runnersUp2016.append(Album("Oathbreaker","Rheia","https://coverartarchive.org/release-group/081fc686-c66a-4981-827c-c40337834d91/front.png", "https://open.spotify.com/album/2eo8OwibPK06ZoHmIAfClG"))
	runnersUp2016.append(Album("Odd Nosdam","Sisters","https://coverartarchive.org/release/76056e56-d6a8-4591-912a-69ebe1d91011/12890639066.jpg", "https://open.spotify.com/album/6eI4AV8L9K6bF7099n192W"))
	runnersUp2016.append(Album("William Tyler","Modern Country","https://coverartarchive.org/release/dc32ae42-0cbb-47f0-80ac-874176f085f8/13670993563.jpg", "https://open.spotify.com/album/0AlKGJjZriUhapXB3hyW6h"))

	spreadsheet2016 = dict()
	spreadsheet2016["link"] = "https://docs.google.com/spreadsheets/d/1oB34W8PMvObQHQQpNRwneSXreFHbHU0HdLbcbsaW3qw"
	spreadsheet2016["ratingCount"] = "589"
	spreadsheet2016["averageRating"] = "6.29"

	albums2016 = dict()
	albums2016["list"] = list2016
	albums2016["runnersUp"] = runnersUp2016
	albums2016["spreadsheet"] = spreadsheet2016

	list2015 = list()
	list2015.append(Album("Sufjan Stevens", "Carrie & Lowell", "https://coverartarchive.org/release/87b4a614-d53d-4495-b176-5d4f2bb353e6/9658447626.jpg", ""))
	list2015.append(Album("Pile", "You're Better Than This", "https://coverartarchive.org/release-group/dc1fe040-2d5f-465d-a971-ee84d0c0f12c/front.jpg", ""))
	list2015.append(Album("Courtney Barnett", "Sometimes I Sit and Think, and Sometimes I Just Sit", "https://coverartarchive.org/release-group/136815ec-7b75-4477-9f35-8e6adb926700/front.jpg", ""))
	list2015.append(Album("Hop Along", "Painted Shut", "https://coverartarchive.org/release/8114b878-c9ff-4c4f-bc19-5baabc10f32c/10513425245.jpg", ""))
	list2015.append(Album("Titus Andronicus", "The Most Lamentable Tragedy", "https://coverartarchive.org/release-group/9b3cb91c-5cf3-45fe-8c32-8449e2162f57/front.jpg", ""))
	list2015.append(Album("Elder", "Lore", "https://coverartarchive.org/release/ee6e329d-b02e-4d62-bf4f-74770fda6864/9620598741.jpg", ""))
	list2015.append(Album("Viet Cong", "Viet Cong", "https://coverartarchive.org/release/5d5fc614-25fe-4b89-8747-f4357f7a7757/9260448034.jpg", ""))
	list2015.append(Album("Car Seat Headrest", "Teens of Style", "https://coverartarchive.org/release/5f8e989d-cd81-4b7b-85c8-13c7f071bb94/11971023916.jpg", ""))
	list2015.append(Album("Sleater-Kinney", "No Cities to Love", "https://coverartarchive.org/release-group/aeacebc7-34fc-44ff-bde9-779e6fde7ade/front.jpg", ""))
	list2015.append(Album("Loma Prieta", "Self Portrait", "https://f1.bcbits.com/img/a1468573006_10.jpg", ""))
	list2015.append(Album("Punch Brothers", "The Phosphorescent Blues", "https://coverartarchive.org/release-group/c2313d70-3da6-48e4-b310-1982b681e09d/front.jpg", ""))
	list2015.append(Album("Bosse-de-Nage", "All Fours", "https://coverartarchive.org/release/f5380e86-3aa8-462b-bb02-d4701f6a48f7/9793637407.jpg", ""))
	list2015.append(Album("Deerhunter", "Fading Frontier", "https://coverartarchive.org/release-group/d9ea57c7-5582-4159-a901-d058b3468586/front.jpg", ""))
	list2015.append(Album("Ensemble Signal & Steve Reich", "Music for 18 Musicians", "https://coverartarchive.org/release-group/4795a9c0-dfcf-4daa-9b06-9c7bcefe148d/front.jpg", ""))
	list2015.append(Album("Godspeed You! Black Emperor", "Asunder, Sweet and Other Distress", "https://coverartarchive.org/release-group/c74035da-e212-4048-abed-40a7b5343e9a/front.jpg", ""))
	list2015.append(Album("Nicolas Jaar", "Nymphs II/III/IV", "http://i.imgur.com/NGHXYIm.png?1", ""))
	list2015.append(Album("Ought", "Sun Coming Down", "https://coverartarchive.org/release-group/ffa2d4a1-cd45-438a-be58-97c428d40844/front.jpg", ""))
	list2015.append(Album("Julien Baker", "Sprained Ankle", "https://coverartarchive.org/release-group/9d694f1c-fc4b-4372-ab6e-634844f46be9/front.jpg", ""))
	list2015.append(Album("The Staves", "If I Was", "https://coverartarchive.org/release/1e461cfc-a942-4a8c-8111-6df3a26c3c9e/9965719439.png", ""))
	list2015.append(Album("Jamie xx", "In Colour", "https://coverartarchive.org/release-group/a903a977-5932-4cc2-a064-57a596658b3d/front.jpg", ""))
	list2015.append(Album("Girl Band", "Holding Hands with Jamie", "https://coverartarchive.org/release-group/970fe64c-2deb-491e-86d7-41b729118ae0/front.jpg", ""))
	list2015.append(Album("Julia Holter", "Have You in my Wilderness", "https://coverartarchive.org/release-group/3cdb557c-f143-4db9-a49a-a8781a26a247/front.jpg", ""))
	list2015.append(Album("Patrick Watson", "Love Songs for Robots", "https://coverartarchive.org/release-group/ec9a69c6-35fc-4705-aeb6-80373dfa1497/front.jpg", ""))
	list2015.append(Album("Birds in Row", "Personal War", "https://coverartarchive.org/release-group/be249c5a-b686-40f2-9dc8-75a8ed456b2a/front.jpg", ""))
	list2015.append(Album("Christopher Paul Stelling", "Labor Against Waste", "http://s3.amazonaws.com/content.sitezoogle.com/u/149235/0ee2eae2f415bd1a80275a64fda852a7694a7e9c/large/10723940-921955494493144-1660504926-n.jpg?1427746844", ""))
	list2015.append(Album("American Wrestlers", "American Wrestlers", "https://coverartarchive.org/release-group/4932c0f7-a721-49d9-b3f9-15f226a589fc/front.jpg", ""))
	list2015.append(Album("Jeff Rosenstock", "We Cool?", "https://coverartarchive.org/release-group/1052f90a-b695-497b-ab6a-ec2dc0e69de3/front.jpg", ""))
	list2015.append(Album("Jason Isbell", "Something More than Free", "http://www.jasonisbell.com/wp-content/uploads/2013/06/isbell-something-more-than-free.jpg", ""))
	list2015.append(Album("Bop English", "Constant Bop", "https://coverartarchive.org/release-group/d1134046-3ee8-48a7-9c30-6bb484f9c240/front.jpg", ""))
	list2015.append(Album("Colin Stetson / Sarah Neufeld", "Never Were the Way She Was", "https://coverartarchive.org/release-group/22b13783-b1ca-4953-90e8-2ca5a2bce257/front.jpg", ""))

	runnersUp2015 = list()
	runnersUp2015.append(Album("Baroness", "Purple", "https://coverartarchive.org/release-group/df98ad28-b0b2-4aa6-8353-eea4146b93f1/front.jpg", ""))
	runnersUp2015.append(Album("Have you ever seen the Jane Fonda Aerobic VHS?", "Teenage Sweetheart", "https://f4.bcbits.com/img/a2637841094_10.jpg", ""))
	runnersUp2015.append(Album("Oneohtrix Point Never", "Garden of Delete", "https://coverartarchive.org/release-group/5acba13f-0e96-4119-856a-6cd561ccd694/front.jpg", ""))
	runnersUp2015.append(Album("Royal Headache", "High", "https://coverartarchive.org/release-group/378f3df6-f7e5-4fb5-b313-2ca370ea216b/front.jpg", ""))
	runnersUp2015.append(Album("Sports", "All of Something", "https://coverartarchive.org/release-group/35628285-2da7-4db4-a5e6-5585791d2d61/front.jpg", ""))

	spreadsheet2015 = dict()
	spreadsheet2015["link"] = "https://docs.google.com/spreadsheets/d/1d-jxvDuYvmbqPeSled3RfJIzcZMeKXekiLe02JTR4hM/edit#gid=0"
	spreadsheet2015["ratingCount"] = "550"
	spreadsheet2015["averageRating"] = "6.21"

	albums2015 = dict()
	albums2015["list"] = list2015
	albums2015["runnersUp"] = runnersUp2015
	albums2015["spreadsheet"] = spreadsheet2015

	list2014 = list()
	list2014.append(Album("Swans", "To Be Kind", "http://coverartarchive.org/release-group/d2df1a2d-4da1-40a3-a825-5674ce117579/front-500.jpg", ""))
	list2014.append(Album("Iceage","Plowing Into The Field Of Love","http://coverartarchive.org/release-group/5792bd69-7664-4a23-87aa-5f43c9b48338/front-500.jpg", ""))
	list2014.append(Album("Sun Kil Moon", "Benji", "http://coverartarchive.org/release-group/9e14617c-3842-4d5f-bef4-16b38f2c9f4e/front-500.jpg", ""))
	list2014.append(Album("Ought","More Than Any Other Day","http://coverartarchive.org/release/1f459335-11f6-441e-a07b-4ff102352ac2/6831251404-500.jpg", ""))
	list2014.append(Album("Thee Silver Mt. Zion Memorial Orchestra","Fuck Off Get Free We Pour Light On Everything","http://coverartarchive.org/release-group/0c6dca7d-e1bb-4dfd-aaf5-35c60bb910cd/front-500.jpg", ""))
	list2014.append(Album("Angel Olsen","Burn Your Fire For No Witness","http://coverartarchive.org/release-group/8cb480c5-404f-4f65-ad88-ba77e19ef33c/front-500.jpg", ""))
	list2014.append(Album("Cloud Nothings","Here And Nowhere Else","http://coverartarchive.org/release-group/f8255f7a-5669-4f1d-92e8-7188fa284017/front-500.jpg", ""))
	list2014.append(Album("The Austerity Program","Beyond Calculation","https://40.media.tumblr.com/4569c9d7993221d5299e71f034096be9/tumblr_n7l2158ORW1qasfv5o3_500.jpg", ""))
	list2014.append(Album("Old Man Gloom","The Ape of God","http://ecx.images-amazon.com/images/I/614yxe1RvHL.jpg", ""))
	list2014.append(Album("White Lung","Deep Fantasy","http://coverartarchive.org/release-group/786fe66b-ab44-4b6c-9cf1-a4d14662f2f0/front-500.jpg", ""))
	list2014.append(Album("Together Pangea","Badillac","http://coverartarchive.org/release-group/5e947f97-ebc7-4e51-932d-41b37cabaa51/front-500.jpg", ""))
	list2014.append(Album("The War On Drugs","Lost In The Dream","http://coverartarchive.org/release-group/943b191f-616f-4091-8516-0979987b5eef/front-500.jpg", ""))
	list2014.append(Album("La Dispute","Rooms Of The House","http://coverartarchive.org/release-group/8dc09bff-dd15-4dc7-b195-8814224a9325/front-500.jpg", ""))
	list2014.append(Album("Thou","Heathen","http://coverartarchive.org/release/c13dc4ab-ce79-4a64-ba08-79b87d966095/7796754563-500.jpg", ""))
	list2014.append(Album("Sharon Van Etten","Are We There","http://coverartarchive.org/release-group/60cbb40c-1db0-4e5b-81a7-b693a67dff0a/front-500.jpg", ""))
	list2014.append(Album("Ty Segall","Manipulator","http://coverartarchive.org/release-group/955fba0f-6aab-407a-b6cf-cce8b4f79717/front-500.jpg", ""))
	list2014.append(Album("Young Widows","Easy Pain","http://coverartarchive.org/release-group/3b2f53a2-d2de-4a9a-9e68-9f0f47d1e818/front-500.jpg", ""))
	list2014.append(Album("Shellac","Dude Incredible","http://coverartarchive.org/release-group/93eddd2b-7ee2-4489-85f7-f52ce9e60658/front-500.jpg", ""))
	list2014.append(Album("Survival Knife","Loose Power","http://coverartarchive.org/release-group/5783231b-50e7-47f4-b15b-2798ad63124d/front-500.jpg", ""))
	list2014.append(Album("Death From Above 1979","The Physical World","http://coverartarchive.org/release-group/c57c63e1-b367-489a-a75f-ddd711e91174/front-500.jpg", ""))
	list2014.append(Album("Krieg","Transient","http://www.nocleansinging.com/wp-content/uploads/2014/08/Krieg-Transient.jpg", ""))
	list2014.append(Album("Have A Nice Life","The Unnatural World","http://ffhdbrhd7sg2o09k.zippykid.netdna-cdn.com/wp-content/uploads/2014/02/fr39coverart.jpg", ""))
	list2014.append(Album("Helms Alee","Sleepwalking Sailors","http://coverartarchive.org/release-group/456243fe-c125-477c-8841-4ba46e26b1dd/front-500.jpg", ""))
	list2014.append(Album("Kevin Morby","Still Life","http://coverartarchive.org/release-group/0a9ac7e0-980e-473d-afee-f17e3171f93b/front-500.jpg", ""))
	list2014.append(Album("Cymbals Eat Guitars","LOSE","http://coverartarchive.org/release-group/0f8a2660-78ec-4863-add5-9cf5ad0b14e4/front-500.jpg", ""))
	list2014.append(Album("Run The Jewels","RTJ2","http://coverartarchive.org/release-group/581d7ac8-8f1d-4d4a-a224-de9c9cd76b39/front-500.jpg", ""))
	list2014.append(Album("A Sunny Day In Glasgow","Sea When Absent","http://coverartarchive.org/release-group/cc514c1c-1b6c-476d-bc93-d96ef0e21757/front-500.jpg", ""))
	list2014.append(Album("A Winged Victory For The Sullen","Atmos","http://coverartarchive.org/release-group/7bc3d477-b550-40b0-abdb-febe66b92290/front-500.jpg", ""))
	list2014.append(Album("Dope Body","Lifer","http://cdn.pitchfork.com/tracks/17017/homepage_large.f11d44b5.jpg", ""))
	list2014.append(Album("Goat","Commune","https://ia902302.us.archive.org/2/items/mbid-73159b10-18ef-4dd0-91dc-3facb6ecb6df/mbid-73159b10-18ef-4dd0-91dc-3facb6ecb6df-8309930145_thumb500.jpg", ""))

	runnersUp2014 = list()
	runnersUp2014.append(Album("Horrendous", "Ecdysis", "http://ia601404.us.archive.org/17/items/mbid-81f6450a-533e-4207-b768-46d759b8734a/mbid-81f6450a-533e-4207-b768-46d759b8734a-8626516684_thumb500.jpg", ""))
	runnersUp2014.append(Album("Prawn","Kingfisher","http://ia802302.us.archive.org/22/items/mbid-e39d2d84-667a-45fb-9e80-4240bb630f9a/mbid-e39d2d84-667a-45fb-9e80-4240bb630f9a-8118949720_thumb500.jpg", ""))
	runnersUp2014.append(Album("Spoon","They Want My Soul","http://ia802300.us.archive.org/24/items/mbid-81adb7c3-42de-4469-bd2a-3a478434ed9e/mbid-81adb7c3-42de-4469-bd2a-3a478434ed9e-8015677069_thumb500.jpg", ""))
	runnersUp2014.append(Album("St. Vincent","St. Vincent","http://ia802604.us.archive.org/13/items/mbid-d88e330d-0cdd-4c9f-981a-a1f0d08e484c/mbid-d88e330d-0cdd-4c9f-981a-a1f0d08e484c-6266726896_thumb500.jpg", ""))
	runnersUp2014.append(Album("Thurston Moore","The Best Day","http://ia902607.us.archive.org/13/items/mbid-202621ed-26c9-4011-8fef-1f3cd42d3838/mbid-202621ed-26c9-4011-8fef-1f3cd42d3838-8612455078_thumb500.jpg", ""))

	spreadsheet2014 = dict()
	spreadsheet2014["link"] = "https://docs.google.com/spreadsheets/d/1P1o28DtLrEor_7v1i8l69wshNj-TmL0TJ64PNXp2eeI/edit#gid=0"
	spreadsheet2014["ratingCount"] = "450"
	spreadsheet2014["averageRating"] = "6.15"

	albums2014 = dict()
	albums2014["list"] = list2014
	albums2014["runnersUp"] = runnersUp2014
	albums2014["spreadsheet"] = spreadsheet2014

	list2013 = list()
	list2013.append(Album("Jon Hopkins", "Immunity", "http://ia801801.us.archive.org/3/items/mbid-9b93c88b-b939-4206-af30-b3a3e7f1ab8d/mbid-9b93c88b-b939-4206-af30-b3a3e7f1ab8d-4299705401_thumb500.jpg", ""))
	list2013.append(Album("Kurt Vile", "Wakin on a Pretty Daze", "https://ia801702.us.archive.org/2/items/mbid-b62e3ec7-d6bb-43c6-8eb8-30d958d109d0/mbid-b62e3ec7-d6bb-43c6-8eb8-30d958d109d0-3846880817_thumb500.jpg", ""))
	list2013.append(Album("Nils Frahm", "Spaces", "https://ia801002.us.archive.org/5/items/mbid-30d9a7e2-e10a-431d-8cc2-6e57a8abfc4b/mbid-30d9a7e2-e10a-431d-8cc2-6e57a8abfc4b-6036413048_thumb500.jpg", ""))
	list2013.append(Album("Altar Of Plagues", "Teethed Glory And Injury", "http://coverartarchive.org/release-group/6d809bf6-4d98-4509-aa3b-587dcd82d081/front-500.jpg", ""))
	list2013.append(Album("Darkside", "Psychic", "http://coverartarchive.org/release/873f8153-2758-4f33-8399-5d00e4b9370e/front-500.jpg", ""))
	list2013.append(Album("Iceage", "You're Nothing", "http://coverartarchive.org/release-group/01357463-b63c-4a6b-ade1-8b5f4eb55b96/front-500.jpg", ""))
	list2013.append(Album("Cult Of Luna", "Vertikal", "http://coverartarchive.org/release/ca88ef67-66c1-4c4c-ac3e-66d178d575d6/3169895120-500.jpg", ""))
	list2013.append(Album("The National", "Trouble Will Find Me", "http://coverartarchive.org/release-group/a5a2875f-41cb-4c48-9a72-e845d224db96/front-500.jpg", ""))
	list2013.append(Album("Widowspeak", "Almanac", "http://coverartarchive.org/release-group/b3bb63c1-4b8c-4a19-8227-155ef324ff48/front-500.jpg", ""))
	list2013.append(Album("Volcano Choir", "Repave", "http://coverartarchive.org/release-group/82686fd2-265e-4220-aac7-5c93dd395608/front-500.jpg", ""))
	list2013.append(Album("Deafheaven", "Sunbather", "http://coverartarchive.org/release-group/8a061d0e-fa0c-4571-91ff-8bc3911b6428/front-500.jpg", ""))
	list2013.append(Album("Vampire Weekend", "Modern Vampires Of The City", "http://coverartarchive.org/release-group/eb143c5a-9a85-4bce-a78c-f7faf72c0169/front-500.jpg", ""))
	list2013.append(Album("Tim Hecker", "Virgins", "http://coverartarchive.org/release-group/8121eda6-f17d-4eaa-bd44-598828df0bc9/front-500.jpg", ""))
	list2013.append(Album("Year Of No Light", "Tocsin", "http://coverartarchive.org/release-group/26b8d47c-b44c-4ade-ade6-1feb1ab230ee/front-500.jpg", ""))
	list2013.append(Album("Chelsea Wolfe", "Pain Is Beauty", "http://coverartarchive.org/release-group/50ef8504-86ca-4f2f-b46f-006458e416f3/front-500.jpg", ""))
	list2013.append(Album("Queens Of The Stone Age", "Like Clockwork", "http://coverartarchive.org/release-group/c92f73ee-527f-42ed-a556-fd615941e214/front-500.jpg", ""))
	list2013.append(Album("Subrosa", "More Constant Than The Gods", "http://coverartarchive.org/release-group/fd11cada-e35a-4eb7-9ee9-9e024f404ee8/front-500.jpg", ""))
	list2013.append(Album("Nick Cave And The Bad Seeds", "Push The Sky Away", "http://coverartarchive.org/release-group/ae8faaeb-9134-400d-819b-773e20a7d4e4/front-500.jpg", ""))
	list2013.append(Album("Gorguts", "Colored Sands", "http://coverartarchive.org/release-group/6153aa16-7ec4-483d-9592-29039fc27f25/front-500.jpg", ""))
	list2013.append(Album("Young Fathers", "Tape Two", "http://coverartarchive.org/release-group/8ec3c767-a998-4e09-bf62-705106abea32/front-500.jpg", ""))
	list2013.append(Album("Waxahatchee", "Cerulean Salt", "http://coverartarchive.org/release-group/78bf1ed3-3d6c-48a7-a651-7489631ac9fd/front-500.jpg", ""))
	list2013.append(Album("Boards Of Canada", "Tomorrow's Harvest", "http://coverartarchive.org/release/d1f52538-291c-45a3-80a1-ac601f84ab87/front-500.jpg", ""))
	list2013.append(Album("Roy Harper", "Man And Myth", "http://ecx.images-amazon.com/images/I/819kzrtOplL._SL1397_.jpg", ""))
	list2013.append(Album("Oneohtrix Point Never", "R Plus Seven", "http://coverartarchive.org/release/10cc746f-786c-4307-b8de-92a687489cb4/front-250.jpg", ""))
	list2013.append(Album("Deerhunter", "Monomania", "http://coverartarchive.org/release-group/ddee6c28-e113-4437-8dcf-bb412ec5c9d4/front-250.jpg", ""))
	list2013.append(Album("The Drones", "I See Seaweed", "http://coverartarchive.org/release-group/8be5799b-6c5d-48a6-8f88-6472c33d54bd/front-250.jpg", ""))
	list2013.append(Album("Armand Hammer", "Race Music", "http://coverartarchive.org/release-group/8bb34c00-1cc6-4b2b-92a4-e4d6c536fcc1/front-250.jpg", ""))
	list2013.append(Album("Thee Oh Sees", "Floating Coffin", "http://coverartarchive.org/release/877221c2-a4fe-4c34-b89f-8d43adb31d80/front-250.jpg", ""))
	list2013.append(Album("Disclosure", "Settle", "http://coverartarchive.org/release-group/cefd427e-185e-4a94-a6a9-a03d8a53b60a/front-250.jpg", ""))
	list2013.append(Album("Eluvium", "Nightmare Ending", "https://images-na.ssl-images-amazon.com/images/I/51cxWby5TJL.jpg", ""))
	list2013.append(Album("Fuck Buttons", "Slow Focus", "http://coverartarchive.org/release-group/77a52eec-07c6-477a-9c9e-f0de4c473d61/front-250.jpg", ""))
	list2013.append(Album("Future Of The Left", "How To Stop Your Brain In An Accident", "http://coverartarchive.org/release/234bcd09-f7b7-4b9c-a427-baf839abc453/front-250.jpg", ""))
	list2013.append(Album("Kanye West", "Yeezus", "http://coverartarchive.org/release/44f67341-2586-4283-bc3f-cf03ae89dc35/4404841321-250.jpg", ""))
	list2013.append(Album("Weekend Nachos", "Still", "http://www.metalinjection.net/wp-content/uploads/2013/11/Weekend-Nachos-Still.jpg", ""))
	list2013.append(Album("Melt-Banana", "fetch", "http://coverartarchive.org/release-group/ebde320c-2869-423b-beed-47e1df6b459e/front-250.jpg", ""))
	list2013.append(Album("Buke And Gase", "General Dome", "http://coverartarchive.org/release-group/8172fb2f-4af0-4abc-ae78-1a1e58b75bb7/front-250.jpg", ""))
	list2013.append(Album("Jenny Hval", "Innocence Is Kinky", "http://coverartarchive.org/release-group/022cf563-579e-4655-91a0-bef34732306b/front-250.jpg", ""))
	list2013.append(Album("The Knife", "Shaking The Habitual", "http://coverartarchive.org/release-group/06448e12-18d8-4d52-a51f-d4c83d07ec09/front-250.jpg", ""))
	list2013.append(Album("Sigur Ros", "Kveikur", "http://coverartarchive.org/release-group/9fa7397e-7212-425f-8158-87c3bfb79602/front-250.jpg", ""))
	list2013.append(Album("Ghostpoet", "Some Say I So I Say Light", "https://ia800106.us.archive.org/9/items/mbid-12513a3d-404a-4db4-93f1-7b73321807dd/mbid-12513a3d-404a-4db4-93f1-7b73321807dd-17605309898_thumb500.jpg", ""))

	runnersUp2013 = list()

	spreadsheet2013 = dict()
	spreadsheet2013["link"] = "https://docs.google.com/spreadsheets/d/1PanBa3CHq0Z-FTatPKebno41cNl6xNpS3PDb9AxUJd0/edit#gid=0&vpid=A2"
	spreadsheet2013["ratingCount"] = "466"
	spreadsheet2013["averageRating"] = "6.15"

	albums2013 = dict()
	albums2013["list"] = list2013
	albums2013["runnersUp"] = runnersUp2013
	albums2013["spreadsheet"] = spreadsheet2013

	list2012 = list()
	list2012.append(Album("Swans","The Seer","http://ia800308.us.archive.org/30/items/mbid-31f30ecf-69df-4920-89da-7bd6d9abc3f6/mbid-31f30ecf-69df-4920-89da-7bd6d9abc3f6-10402018472_thumb500.jpg", ""))
	list2012.append(Album("Godspeed You! Black Emperor","'Allelujah! Don't Bend! Ascend!","http://ia902705.us.archive.org/34/items/mbid-0b6d1c29-9c37-4392-ac4f-5822933f89e6/mbid-0b6d1c29-9c37-4392-ac4f-5822933f89e6-2200016389_thumb500.jpg", ""))
	list2012.append(Album("Fiona Apple","The Idler Wheel Is Wiser Than the Driver of the Screw and Whipping Cords Will Serve You More Than Ropes Will Ever Do","http://ia800504.us.archive.org/2/items/mbid-04c72095-a6af-41f7-a18a-a1dd7e305620/mbid-04c72095-a6af-41f7-a18a-a1dd7e305620-1264480591_thumb500.jpg", ""))
	list2012.append(Album("Torche","Harmonicraft","http://ia902706.us.archive.org/33/items/mbid-c0b51d77-efa8-4849-8a24-095ac377138e/mbid-c0b51d77-efa8-4849-8a24-095ac377138e-2361027232_thumb500.jpg", ""))
	list2012.append(Album("Bosse-de-Nage","iii","http://ecx.images-amazon.com/images/I/512w%2Bl7j2GL.jpg", ""))
	list2012.append(Album("Tame Impala","Lonerism","http://ia802708.us.archive.org/31/items/mbid-340898f5-7a35-4cc0-9a06-fe06fe0137b9/mbid-340898f5-7a35-4cc0-9a06-fe06fe0137b9-10223917630_thumb500.jpg", ""))
	list2012.append(Album("Cloud Nothings","Attack On Memory","http://ia902601.us.archive.org/30/items/mbid-36f88c0d-9036-4ef6-83f8-bc8669c36d39/mbid-36f88c0d-9036-4ef6-83f8-bc8669c36d39-2098697244_thumb500.jpg", ""))
	list2012.append(Album("Grizzly Bear","Shields","http://ia802706.us.archive.org/27/items/mbid-8baedb5b-192c-4426-99ee-4c23d50550bd/mbid-8baedb5b-192c-4426-99ee-4c23d50550bd-2176498254_thumb500.jpg", ""))
	list2012.append(Album("Spiritualized","Sweet Heart Sweet Light","http://coverartarchive.org/release-group/9b5bf979-122c-4b5d-b73d-4c22ff193828/front.jpg", ""))
	list2012.append(Album("Converge","All We Love We Leave Behind","http://coverartarchive.org/release-group/86037f34-72c6-4ad9-8072-f20bb839f78d/front.jpg", ""))
	list2012.append(Album("Action Bronson / Party Supplies","Blue Chips","http://coverartarchive.org/release-group/04428174-ec07-40de-b317-7a2f0f8c4808/front.jpg", ""))
	list2012.append(Album("The Men","Open Your Heart","http://coverartarchive.org/release/2b868dc8-271a-4402-b7b3-bb72d182f54c/2098745006.jpg", ""))
	list2012.append(Album("Royal Thunder","CVI","http://coverartarchive.org/release-group/a9cd4fcc-5aa4-4def-a511-df31ca98b2ce/front.jpg", ""))
	list2012.append(Album("Wodensthrone","Curse","http://coverartarchive.org/release-group/51a46170-8e31-4268-9b8e-55f5906bae91/front.jpg", ""))
	list2012.append(Album("Ash Borer","Cold Of Ages","http://coverartarchive.org/release-group/5557bdd2-26bf-48e5-a3bf-988ffb35cc93/front.jpg", ""))
	list2012.append(Album("Alt-j","An Awesome Wave","http://coverartarchive.org/release-group/0d8562eb-7f72-427b-8a0b-984cc5ee7766/front.jpg", ""))
	list2012.append(Album("Burial","Kindred EP","http://coverartarchive.org/release-group/1c288979-ce2f-4e4b-90e4-845908cf7ffc/front.jpg", ""))
	list2012.append(Album("...And You Will Know Us By The Trail Of Dead","Lost Songs","http://coverartarchive.org/release-group/b78489e8-5d85-4b51-9f4a-c556af08361a/front.jpg", ""))
	list2012.append(Album("iamamiwhoami","Kin","http://coverartarchive.org/release-group/2366eec5-5b8f-47e2-a18d-5910cd0ee85a/front.jpg", ""))
	list2012.append(Album("The Evens","The Odds","http://cdn4.pitchfork.com/news/47837/d873864c.jpg", ""))
	list2012.append(Album("Circle Takes The Square","Decompositions: Volume Number One","http://coverartarchive.org/release-group/b2232a36-80ce-4116-be1e-1421dea2aaf6/front.jpg", ""))
	list2012.append(Album("Jack White","Blunderbuss","http://coverartarchive.org/release-group/37f48931-e5e6-488f-a531-ad2db311158d/front.jpg", ""))
	list2012.append(Album("Japandroids","Celebration Rock","http://coverartarchive.org/release-group/32f90db3-467a-4a31-b36b-e4b73dc0cc78/front.jpg", ""))
	list2012.append(Album("Pig Destroyer","Book Burner","http://coverartarchive.org/release-group/2ff27be2-de49-43e4-a5a3-6ca6452efc3d/front.jpg", ""))
	list2012.append(Album("High On Fire","De Vermis Mysteriis","http://coverartarchive.org/release-group/26371a98-daca-4798-8c22-8bc9dfb93b26/front.jpg", ""))
	list2012.append(Album("Susanne Sundfor","The Silicone Veil","http://coverartarchive.org/release-group/ecbd323b-3463-497c-b40e-f2a2c41df61f/front.jpg", ""))
	list2012.append(Album("The Sword","Apocryphon","http://cdn.albumoftheyear.org/album/apocryphon.jpg", ""))
	list2012.append(Album("The Walkmen","Heaven","http://coverartarchive.org/release/5921d6cd-d098-46f4-a69e-7205ac29bbfe/946789854.jpg", ""))
	list2012.append(Album("Loma Prieta","I.V.","http://coverartarchive.org/release-group/d5368fc7-4181-463e-b060-9f0ad44b3580/front.jpg", ""))
	list2012.append(Album("Anais Mitchell","Young Man In America","http://coverartarchive.org/release-group/06fd9495-1025-416b-866a-a214f29b3036/front.jpg", ""))
	list2012.append(Album("Aesop Rock","Skelethon","http://coverartarchive.org/release-group/769966a4-c76b-4935-a5c0-74147dcb5b79/front.jpg", ""))
	list2012.append(Album("Leech","If We Get There One Day, Would You Please Open The Gates?","http://coverartarchive.org/release-group/c9e8f50d-4734-4ef7-9193-519c3b453245/front.jpg", ""))
	list2012.append(Album("Pigs","You Ruin Everything","https://41.media.tumblr.com/d8deb797657e7127af9fec86c2d2e3c4/tumblr_n13hysC8p81qdix05o1_500.jpg", ""))
	list2012.append(Album("White Rabbits","Milk Famous","http://ecx.images-amazon.com/images/I/51tdXd%2BUnYL.jpg", ""))
	list2012.append(Album("Cate Le Bon","CYRK","http://ecx.images-amazon.com/images/I/61XRvSU9fzL.jpg", ""))
	list2012.append(Album("Kowloon Walled City","Container Ships","http://coverartarchive.org/release-group/f8ea1b69-0dbf-44cc-895e-1db5d717f115/front.jpg", ""))
	list2012.append(Album("Wizard Rifle","Speak Loud Say Nothing","https://f4.bcbits.com/img/a1266608581_10.jpg", ""))
	list2012.append(Album("Bats","The Sleep Of Reason","http://coverartarchive.org/release-group/2a4a8fda-e47f-4c95-994f-7bf8ae500f3d/front.jpg", ""))
	list2012.append(Album("Andrew Bird","Break It Yourself","http://coverartarchive.org/release-group/97fe2ba8-1c28-45ec-a8ba-38b7e4893e3d/front.jpg", ""))
	list2012.append(Album("Alexandre Desplat","Moonrise Kingdom","http://ia601606.us.archive.org/35/items/mbid-349000da-5b41-4fd3-8cc2-21082ec74eee/mbid-349000da-5b41-4fd3-8cc2-21082ec74eee-3435627137_thumb500.jpg", ""))

	runnersUp2012 = list()
	runnersUp2012.append(Album("Colour Haze","She Said","http://coverartarchive.org/release-group/16e8b800-1009-4b8b-af9e-ea98329d096d/front.jpg", ""))
	runnersUp2012.append(Album("Clams Casino","Instrumental Tape 2","http://coverartarchive.org/release-group/90712528-f590-4a6d-aba0-14f459425752/front.jpg", ""))
	runnersUp2012.append(Album("Dinosaur Jr.","I Bet On Sky","http://coverartarchive.org/release-group/727e7b83-4709-4398-a285-da71e38b74da/front.jpg", ""))
	runnersUp2012.append(Album("Grave","Endless Procession Of Souls","http://ecx.images-amazon.com/images/I/61ZPMCrp4SL.jpg", ""))
	runnersUp2012.append(Album("John Talabot","fin","http://coverartarchive.org/release/697082bd-a67e-453a-a63c-6696b06ac98d/2985165419.jpg", ""))
	runnersUp2012.append(Album("Max Richter","Recomposed by Max Richter. Vivaldi - The Four Seasons","http://coverartarchive.org/release-group/b921615e-355b-47af-a13d-6a223ead16e6/front.jpg", ""))
	runnersUp2012.append(Album("Screaming Females","Ugly","http://coverartarchive.org/release-group/d41c8b41-efbd-46c0-a163-1d332151d112/front.jpg", ""))
	runnersUp2012.append(Album("Sharon Van Etten","Tramp","http://coverartarchive.org/release-group/58eff3eb-7445-4914-b38a-068e1b3bb83e/front.jpg", ""))
	runnersUp2012.append(Album("Suis La Lune","Riala","http://coverartarchive.org/release-group/84069713-38e2-4ab6-81a3-925fae886ae7/front.jpg", ""))
	runnersUp2012.append(Album("Ty Segall / White Fence","Hair","http://coverartarchive.org/release-group/0b86bf0e-f49c-43e2-83eb-586abd54b8a4/front.jpg", ""))

	spreadsheet2012 = dict()
	spreadsheet2012["link"] = "https://docs.google.com/spreadsheets/d/1HVcKqtqWto57-81y_5WlLINayV0dOp8MY_B7Uo3VK0Q/edit"
	spreadsheet2012["ratingCount"] = "480"
	spreadsheet2012["averageRating"] = "6.26"

	albums2012 = dict()
	albums2012["list"] = list2012
	albums2012["runnersUp"] = runnersUp2012
	albums2012["spreadsheet"] = spreadsheet2012

	list2011 = list()
	list2011.append(Album("Giles Corey","Giles Corey","http://coverartarchive.org/release-group/a5c26b66-3f39-463a-aff4-cf859da4a0c3/front.jpg", ""))
	list2011.append(Album("Fleet Foxes","Helplessness Blues","http://coverartarchive.org/release-group/d569deba-8c6b-4d08-8c43-d0e5a1b8c7f3/front.jpg", ""))
	list2011.append(Album("Tom Waits","Bad As Me","http://coverartarchive.org/release-group/956f10e8-0c74-4010-99d3-1b60fb7e88bc/front.jpg", ""))
	list2011.append(Album("PJ Harvey","Let England Shake","http://vignette4.wikia.nocookie.net/lyricwiki/images/e/e5/PJ_Harvey_-_Let_England_Shake.jpg/revision/latest?cb=20110225143252", ""))
	list2011.append(Album("Wye Oak","Civilian","http://coverartarchive.org/release-group/6ac512b1-60b5-4c7b-a923-f2699cb3addc/front.png", ""))
	list2011.append(Album("Kurt Vile","Smoke Ring For My Halo","http://ecx.images-amazon.com/images/I/51y-IFqkMaL.jpg", ""))
	list2011.append(Album("Youth Lagoon","Year of Hibernation","http://coverartarchive.org/release-group/703b7833-1dac-4d8a-9015-e0c9d45b9764/front.jpg", ""))
	list2011.append(Album("Woods Of Desolation","Torn Beyond Reason","http://coverartarchive.org/release-group/2b183e9d-620d-4d58-9f6d-e5ceed497b9f/front.jpg", ""))
	list2011.append(Album("O'Brother","Garden Window","http://coverartarchive.org/release/b3309fa4-d178-4cbd-81d3-44f6c1aa9642/3392413535.jpg", ""))
	list2011.append(Album("This Will Destroy You","Tunnel Blanket","http://coverartarchive.org/release-group/932067d2-4d80-495d-a037-e9c46d8d9314/front.jpg", ""))
	list2011.append(Album("Altar Of Plagues","Mammal","http://coverartarchive.org/release-group/9d6aedcf-234c-446d-8978-f80d83046f89/front.jpg", ""))
	list2011.append(Album("Wilco","The Whole Love","http://coverartarchive.org/release-group/760f9d8c-3465-497f-9186-a63b1270d9fb/front.jpg", ""))
	list2011.append(Album("Fell Voices","Fell Voices","http://coverartarchive.org/release-group/7b06a50e-0ab1-421b-a57d-c67ea859af5b/front.jpg", ""))
	list2011.append(Album("Fucked Up","David Comes To Life","http://coverartarchive.org/release-group/31fcb4ca-5845-4673-bdcc-594fd807d046/front.jpg", ""))
	list2011.append(Album("Bon Iver","Bon Iver, Bon Iver","http://coverartarchive.org/release-group/2cb36662-3560-4b90-a0a5-7924ac039490/front.jpg", ""))
	list2011.append(Album("Colin Stetson","New History Warfare Vol. 2: Judges","http://coverartarchive.org/release-group/874ac3bc-70fc-4e90-aef2-ef2b6b8927eb/front.jpg", ""))
	list2011.append(Album("Grails","Deep Politics","http://coverartarchive.org/release-group/eeeb33e4-2b8f-4ea5-8116-0a4c92a91f67/front.jpg", ""))
	list2011.append(Album("Graveyard","Hisingen Blues","http://coverartarchive.org/release-group/b60885c0-e92d-4801-8413-0116418bccce/front.jpg", ""))
	list2011.append(Album("Wormrot","Dirge","http://coverartarchive.org/release-group/1ae7a0d3-cd2c-4cc6-95ba-125810117a19/front.jpg", ""))
	list2011.append(Album("KEN Mode","Venerable","http://ecx.images-amazon.com/images/I/519dki3RrDL.jpg", ""))
	list2011.append(Album("Mamiffer","Mare Decendrii","http://ecx.images-amazon.com/images/I/617h3E5Q42L.jpg", ""))
	list2011.append(Album("St. Vincent","Strange Mercy","http://coverartarchive.org/release-group/a9c80acf-5017-4301-8da0-2d6dfb502400/front.jpg", ""))
	list2011.append(Album("Subrosa","No Help For The Mighty Ones","http://coverartarchive.org/release-group/908c0d81-ba8f-48e4-aa69-ed95aae58569/front.jpg", ""))
	list2011.append(Album("The Black Keys","El Camino","http://coverartarchive.org/release-group/c2eed4c1-5cd9-469a-9075-b82077093967/front.jpg", ""))
	list2011.append(Album("The Field","Looping State Of Mind","http://coverartarchive.org/release-group/6745fa25-3fbe-4c76-b29b-83ed5dea788f/front.jpg", ""))
	list2011.append(Album("Cave In","White Silence","http://coverartarchive.org/release-group/5981684e-a3a6-4d17-9390-1cc2670beff6/front.jpg", ""))
	list2011.append(Album("Tombs","Path Of Totality","http://ecx.images-amazon.com/images/I/61NRRmH%2B0DL.jpg", ""))
	list2011.append(Album("Fuck The Facts","Die Miserable","http://coverartarchive.org/release-group/62005bd4-f866-468c-a80b-83549ef32b75/front.jpg", ""))
	list2011.append(Album("Mastodon","The Hunter","http://coverartarchive.org/release-group/3c73bc27-4567-4957-8cfb-929d79b3a6ce/front.jpg", ""))
	list2011.append(Album("Trap Them","Darker Handcraft","http://www.brooklynvegan.com/img/metal/various/Trap_Them_-_Darker_Handcraft_artwork.jpg", ""))
	list2011.append(Album("*shels","Plains Of The Purple Buffalo","https://coverartarchive.org/release-group/3768f323-10a6-460e-8d73-914f594b81bf/front.jpg", ""))
	list2011.append(Album("Tim Hecker","Ravedeath,1972","http://coverartarchive.org/release-group/b55c9544-ba14-436f-a97e-2157b10d540d/front.jpg", ""))
	list2011.append(Album("The Roots","Undun","http://coverartarchive.org/release-group/3d5c691e-61bd-4235-999b-31ebea927227/front.jpg", ""))
	list2011.append(Album("Cormorant","Dwellings","https://f1.bcbits.com/img/0001532772_10.jpg", ""))
	list2011.append(Album("Corrupted","Garten Der Unbewusstheit","http://coverartarchive.org/release-group/8d440a0f-8731-4736-86ef-36cd9bab3bd0/front.jpg", ""))
	list2011.append(Album("M83","Hurry Up We're Dreaming","http://coverartarchive.org/release-group/5f898a60-acc5-48fc-a11b-2926084c0924/front.jpg", ""))
	list2011.append(Album("Widowspeak","Widowspeak","http://ia600403.us.archive.org/18/items/mbid-ed1d9bee-fdaf-4a26-bc5d-f3c7a25780b9/mbid-ed1d9bee-fdaf-4a26-bc5d-f3c7a25780b9-6426811654_thumb500.jpg", ""))
	list2011.append(Album("Terra Tenebrosa","The Tunnels","http://coverartarchive.org/release-group/d05b7693-e00b-4a66-abad-accad6ea80fe/front.jpg", ""))
	list2011.append(Album("Trent Reznor & Atticus Ross","The Girl With The Dragon Tattoo","http://coverartarchive.org/release-group/5bae78a4-6a78-42bb-9272-ea1252fec6fd/front.jpg", ""))
	list2011.append(Album("Battles","Gloss Drop","http://coverartarchive.org/release-group/6016a44b-2b1b-483f-bd3f-e67d2ac534c2/front.jpg", ""))

	runnersUp2011 = list()
	runnersUp2011.append(Album("Disma","Towards The Megalith","http://coverartarchive.org/release-group/6e2a41a7-0d99-46c0-bab1-2fde73e72d0c/front.jpg", ""))
	runnersUp2011.append(Album("Diskinesia","Dalla Nascita","https://f1.bcbits.com/img/a2410845608_10.jpg", ""))
	runnersUp2011.append(Album("Feist","Metals","http://ecx.images-amazon.com/images/I/51jgOu9IjRL.jpg", ""))
	runnersUp2011.append(Album("La Dispute","Wildlife","http://coverartarchive.org/release-group/56b3b007-8332-4a42-b074-2d8b04cdadf1/front.jpg", ""))
	runnersUp2011.append(Album("Matana Roberts","Coin Coin Chapter One: Gens De Couleur Libres","http://ecx.images-amazon.com/images/I/61ZMrQnbBqL.jpg", ""))
	runnersUp2011.append(Album("The Men","Leave Home","http://coverartarchive.org/release-group/7c8ff532-b512-4c61-9510-e368b5bb81bf/front.jpg", ""))
	runnersUp2011.append(Album("Nicolas Jaar","Space Is Only Noise","http://coverartarchive.org/release-group/0fa5e3d1-22b1-4232-adca-0ec05c4c69e7/front.jpg", ""))
	runnersUp2011.append(Album("Noel Gallagher's High Flying Birds","Noel Gallagher's High Flying Birds","http://ecx.images-amazon.com/images/I/51sbfC6U3JL.jpg", ""))
	runnersUp2011.append(Album("Slow Club","Paradise","http://ecx.images-amazon.com/images/I/51lDcrzhD3L.jpg", ""))
	runnersUp2011.append(Album("Solstafir","Svartir Sandarr","http://coverartarchive.org/release-group/3d46b486-44bc-4765-bb0d-40a74e630d32/front.jpg", ""))
	runnersUp2011.append(Album("Richard Buckner","Our Blood","http://ecx.images-amazon.com/images/I/51lidEERF4L.jpg", ""))
	runnersUp2011.append(Album("Rome","Die Aesthetik der Herrschaftsfreiheit","http://ecx.images-amazon.com/images/I/41S9qHG86NL._SY300_.jpg", ""))
	runnersUp2011.append(Album("Russian Circles","Empros","http://coverartarchive.org/release-group/5dc00b2d-4691-4d35-b137-ba646514f096/front.jpg", ""))
	runnersUp2011.append(Album("Thou","The Archer & The Owle","http://coverartarchive.org/release-group/c333dd88-44e7-488c-91a6-e4cca94def10/front.jpg", ""))
	runnersUp2011.append(Album("Washed Out","Within And Without","http://coverartarchive.org/release-group/df595313-7291-446d-9a8f-0d15068e474a/front.jpg", ""))



	spreadsheet2011 = dict()
	spreadsheet2011["link"] = "https://docs.google.com/spreadsheets/d/1dMrtTnsVO0vlNwcrfBgWhH25qvP3aThXWBM-EL8PGD4/edit"
	spreadsheet2011["ratingCount"] = "354"
	spreadsheet2011["averageRating"] = "6.95"

	albums2011 = dict()
	albums2011["list"] = list2011
	albums2011["runnersUp"] = runnersUp2011
	albums2011["spreadsheet"] = spreadsheet2011


	listData = dict()
	listData["2018"] = albums2018
	listData["2017"] = albums2017
	listData["2016"] = albums2016
	listData["2015"] = albums2015
	listData["2014"] = albums2014
	listData["2013"] = albums2013
	listData["2012"] = albums2012
	listData["2011"] = albums2011
	logging.info(albums2014)
	logging.info(listData)

	return listData


class Album:
	def __init__(self, artistName, albumName, imgUrl, previewLink):
		self.artistName = artistName
		self.albumName = albumName
		self.imgUrl = imgUrl
		self.previewLink = previewLink

	# def __repr__(self):
	# 	return "Name: [%s], Release [%s], Img [%s]" % (self.artistName, self.albumName, self.albumImage)

