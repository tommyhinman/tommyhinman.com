import logging

def getAlbumListData():
	

	list2014 = list()
	list2014.append(Album("Swans", "To Be Kind", "http://coverartarchive.org/release-group/d2df1a2d-4da1-40a3-a825-5674ce117579/front-500.jpg"))
	list2014.append(Album("Iceage","Plowing Into The Field Of Love","http://coverartarchive.org/release-group/5792bd69-7664-4a23-87aa-5f43c9b48338/front-500.jpg"))
	list2014.append(Album("Sun Kil Moon", "Benji", "http://coverartarchive.org/release-group/9e14617c-3842-4d5f-bef4-16b38f2c9f4e/front-500.jpg"))
	list2014.append(Album("Ought","More Than Any Other Day","http://coverartarchive.org/release/1f459335-11f6-441e-a07b-4ff102352ac2/6831251404-500.jpg"))
	list2014.append(Album("Thee Silver Mt. Zion Memorial Orchestra","Fuck Off Get Free We Pour Light On Everything","http://coverartarchive.org/release-group/0c6dca7d-e1bb-4dfd-aaf5-35c60bb910cd/front-500.jpg"))
	list2014.append(Album("Angel Olsen","Burn Your Fire For No Witness","http://coverartarchive.org/release-group/8cb480c5-404f-4f65-ad88-ba77e19ef33c/front-500.jpg"))
	list2014.append(Album("Cloud Nothings","Here And Nowhere Else","http://coverartarchive.org/release-group/f8255f7a-5669-4f1d-92e8-7188fa284017/front-500.jpg"))
	list2014.append(Album("The Austerity Program","Beyond Calculation","https://40.media.tumblr.com/4569c9d7993221d5299e71f034096be9/tumblr_n7l2158ORW1qasfv5o3_500.jpg"))
	list2014.append(Album("Old Man Gloom","The Ape of God","http://ecx.images-amazon.com/images/I/614yxe1RvHL.jpg"))
	list2014.append(Album("White Lung","Deep Fantasy","http://coverartarchive.org/release-group/786fe66b-ab44-4b6c-9cf1-a4d14662f2f0/front-500.jpg"))
	list2014.append(Album("Together Pangea","Badillac","http://coverartarchive.org/release-group/5e947f97-ebc7-4e51-932d-41b37cabaa51/front-500.jpg"))
	list2014.append(Album("The War On Drugs","Lost In The Dream","http://coverartarchive.org/release-group/943b191f-616f-4091-8516-0979987b5eef/front-500.jpg"))
	list2014.append(Album("La Dispute","Rooms Of The House","http://coverartarchive.org/release-group/8dc09bff-dd15-4dc7-b195-8814224a9325/front-500.jpg"))
	list2014.append(Album("Thou","Heathen","http://coverartarchive.org/release/c13dc4ab-ce79-4a64-ba08-79b87d966095/7796754563-500.jpg"))
	list2014.append(Album("Sharon Van Etten","Are We There","http://coverartarchive.org/release-group/60cbb40c-1db0-4e5b-81a7-b693a67dff0a/front-500.jpg"))
	list2014.append(Album("Ty Segall","Manipulator","http://coverartarchive.org/release-group/955fba0f-6aab-407a-b6cf-cce8b4f79717/front-500.jpg"))
	list2014.append(Album("Young Widows","Easy Pain","http://coverartarchive.org/release-group/3b2f53a2-d2de-4a9a-9e68-9f0f47d1e818/front-500.jpg"))
	list2014.append(Album("Shellac","Dude Incredible","http://coverartarchive.org/release-group/93eddd2b-7ee2-4489-85f7-f52ce9e60658/front-500.jpg"))
	list2014.append(Album("Survival Knife","Loose Power","http://coverartarchive.org/release-group/5783231b-50e7-47f4-b15b-2798ad63124d/front-500.jpg"))
	list2014.append(Album("Death From Above 1979","The Physical World","http://coverartarchive.org/release-group/c57c63e1-b367-489a-a75f-ddd711e91174/front-500.jpg"))
	list2014.append(Album("Krieg","Transient","http://www.nocleansinging.com/wp-content/uploads/2014/08/Krieg-Transient.jpg"))
	list2014.append(Album("Have A Nice Life","The Unnatural World","http://ffhdbrhd7sg2o09k.zippykid.netdna-cdn.com/wp-content/uploads/2014/02/fr39coverart.jpg"))
	list2014.append(Album("Helms Alee","Sleepwalking Sailors","http://coverartarchive.org/release-group/456243fe-c125-477c-8841-4ba46e26b1dd/front-500.jpg"))
	list2014.append(Album("Kevin Morby","Still Life","http://coverartarchive.org/release-group/0a9ac7e0-980e-473d-afee-f17e3171f93b/front-500.jpg"))
	list2014.append(Album("Cymbals Eat Guitars","LOSE","http://coverartarchive.org/release-group/0f8a2660-78ec-4863-add5-9cf5ad0b14e4/front-500.jpg"))
	list2014.append(Album("Run The Jewels","RTJ2","http://coverartarchive.org/release-group/581d7ac8-8f1d-4d4a-a224-de9c9cd76b39/front-500.jpg"))
	list2014.append(Album("A Sunny Day In Glasgow","Sea When Absent","http://coverartarchive.org/release-group/cc514c1c-1b6c-476d-bc93-d96ef0e21757/front-500.jpg"))
	list2014.append(Album("A Winged Victory For The Sullen","Atmos","http://coverartarchive.org/release-group/7bc3d477-b550-40b0-abdb-febe66b92290/front-500.jpg"))
	list2014.append(Album("Dope Body","Lifer","https://i.ytimg.com/vi/BtaOjS04smU/maxresdefault.jpg"))
	list2014.append(Album("Goat","Commune","https://ia902302.us.archive.org/2/items/mbid-73159b10-18ef-4dd0-91dc-3facb6ecb6df/mbid-73159b10-18ef-4dd0-91dc-3facb6ecb6df-8309930145_thumb500.jpg"))

	runnersUp2014 = list()
	runnersUp2014.append(Album("Horrendous", "Ecdysis", "http://ia601404.us.archive.org/17/items/mbid-81f6450a-533e-4207-b768-46d759b8734a/mbid-81f6450a-533e-4207-b768-46d759b8734a-8626516684_thumb500.jpg"))
	runnersUp2014.append(Album("Prawn","Kingfisher","http://ia802302.us.archive.org/22/items/mbid-e39d2d84-667a-45fb-9e80-4240bb630f9a/mbid-e39d2d84-667a-45fb-9e80-4240bb630f9a-8118949720_thumb500.jpg"))
	runnersUp2014.append(Album("Spoon","They Want My Soul","http://ia802300.us.archive.org/24/items/mbid-81adb7c3-42de-4469-bd2a-3a478434ed9e/mbid-81adb7c3-42de-4469-bd2a-3a478434ed9e-8015677069_thumb500.jpg"))
	runnersUp2014.append(Album("St. Vincent","St. Vincent","http://ia802604.us.archive.org/13/items/mbid-d88e330d-0cdd-4c9f-981a-a1f0d08e484c/mbid-d88e330d-0cdd-4c9f-981a-a1f0d08e484c-6266726896_thumb500.jpg"))
	runnersUp2014.append(Album("Thurston Moore","The Best Day","http://ia902607.us.archive.org/13/items/mbid-202621ed-26c9-4011-8fef-1f3cd42d3838/mbid-202621ed-26c9-4011-8fef-1f3cd42d3838-8612455078_thumb500.jpg"))

	spreadsheet2014 = dict()
	spreadsheet2014["link"] = "https://docs.google.com/spreadsheets/d/1P1o28DtLrEor_7v1i8l69wshNj-TmL0TJ64PNXp2eeI/edit#gid=0"
	spreadsheet2014["ratingCount"] = "450"
	spreadsheet2014["averageRating"] = "6.15"

	albums2014 = dict()
	albums2014["list"] = list2014
	albums2014["runnersUp"] = runnersUp2014
	albums2014["spreadsheet"] = spreadsheet2014

	list2013 = list()
	list2013.append(Album("Jon Hopkins", "Immunity", "http://ia801801.us.archive.org/3/items/mbid-9b93c88b-b939-4206-af30-b3a3e7f1ab8d/mbid-9b93c88b-b939-4206-af30-b3a3e7f1ab8d-4299705401_thumb500.jpg"))
	list2013.append(Album("Kurt Vile", "Wakin on a Pretty Daze", "https://ia801702.us.archive.org/2/items/mbid-b62e3ec7-d6bb-43c6-8eb8-30d958d109d0/mbid-b62e3ec7-d6bb-43c6-8eb8-30d958d109d0-3846880817_thumb500.jpg"))
	list2013.append(Album("Nils Frahm", "Spaces", "http://coverartarchive.org/release/6f9f69af-f0d6-40d8-8f33-de7a3f0ca052/5854196919-500.jpg"))
	list2013.append(Album("Altar Of Plagues", "Teethed Glory And Injury", "http://coverartarchive.org/release-group/6d809bf6-4d98-4509-aa3b-587dcd82d081/front-500.jpg"))
	list2013.append(Album("Darkside", "Psychic", "http://coverartarchive.org/release/873f8153-2758-4f33-8399-5d00e4b9370e/front-500.jpg"))
	list2013.append(Album("Iceage", "You're Nothing", "http://coverartarchive.org/release-group/01357463-b63c-4a6b-ade1-8b5f4eb55b96/front-500.jpg"))
	list2013.append(Album("Cult Of Luna", "Vertikal", "http://coverartarchive.org/release/ca88ef67-66c1-4c4c-ac3e-66d178d575d6/3169895120-500.jpg"))
	list2013.append(Album("The National", "Trouble Will Find Me", "http://coverartarchive.org/release-group/a5a2875f-41cb-4c48-9a72-e845d224db96/front-500.jpg"))
	list2013.append(Album("Widowspeak", "Almanac", "http://coverartarchive.org/release-group/b3bb63c1-4b8c-4a19-8227-155ef324ff48/front-500.jpg"))
	list2013.append(Album("Volcano Choir", "Repave", "http://coverartarchive.org/release-group/82686fd2-265e-4220-aac7-5c93dd395608/front-500.jpg"))
	list2013.append(Album("Deafheaven", "Sunbather", "http://coverartarchive.org/release-group/8a061d0e-fa0c-4571-91ff-8bc3911b6428/front-500.jpg"))
	list2013.append(Album("Vampire Weekend", "Modern Vampires Of The City", "http://coverartarchive.org/release-group/eb143c5a-9a85-4bce-a78c-f7faf72c0169/front-500.jpg"))
	list2013.append(Album("Tim Hecker", "Virgins", "http://coverartarchive.org/release-group/8121eda6-f17d-4eaa-bd44-598828df0bc9/front-500.jpg"))
	list2013.append(Album("Year Of No Light", "Tocsin", "http://coverartarchive.org/release-group/26b8d47c-b44c-4ade-ade6-1feb1ab230ee/front-500.jpg"))
	list2013.append(Album("Chelsea Wolfe", "Pain Is Beauty", "http://coverartarchive.org/release-group/50ef8504-86ca-4f2f-b46f-006458e416f3/front-500.jpg"))
	list2013.append(Album("Queens Of The Stone Age", "Like Clockwork", "http://coverartarchive.org/release-group/c92f73ee-527f-42ed-a556-fd615941e214/front-500.jpg"))
	list2013.append(Album("Subrosa", "More Constant Than The Gods", "http://coverartarchive.org/release-group/fd11cada-e35a-4eb7-9ee9-9e024f404ee8/front-500.jpg"))
	list2013.append(Album("Nick Cave And The Bad Seeds", "Push The Sky Away", "http://coverartarchive.org/release-group/ae8faaeb-9134-400d-819b-773e20a7d4e4/front-500.jpg"))
	list2013.append(Album("Gorguts", "Colored Sands", "http://coverartarchive.org/release-group/6153aa16-7ec4-483d-9592-29039fc27f25/front-500.jpg"))
	list2013.append(Album("Young Fathers", "Tape Two", "http://coverartarchive.org/release-group/8ec3c767-a998-4e09-bf62-705106abea32/front-500.jpg"))
	list2013.append(Album("Waxahatchee", "Cerulean Salt", "http://coverartarchive.org/release-group/78bf1ed3-3d6c-48a7-a651-7489631ac9fd/front-500.jpg"))
	list2013.append(Album("Boards Of Canada", "Tomorrow's Harvest", "http://coverartarchive.org/release/d1f52538-291c-45a3-80a1-ac601f84ab87/front-500.jpg"))
	list2013.append(Album("Roy Harper", "Man And Myth", "http://ecx.images-amazon.com/images/I/819kzrtOplL._SL1397_.jpg"))
	list2013.append(Album("Oneohtrix Point Never", "R Plus Seven", "http://coverartarchive.org/release/10cc746f-786c-4307-b8de-92a687489cb4/front-250.jpg"))
	list2013.append(Album("Deerhunter", "Monomania", "http://coverartarchive.org/release-group/ddee6c28-e113-4437-8dcf-bb412ec5c9d4/front-250.jpg"))
	list2013.append(Album("The Drones", "I See Seaweed", "http://coverartarchive.org/release-group/8be5799b-6c5d-48a6-8f88-6472c33d54bd/front-250.jpg"))
	list2013.append(Album("Armand Hammer", "Race Music", "http://coverartarchive.org/release-group/8bb34c00-1cc6-4b2b-92a4-e4d6c536fcc1/front-250.jpg"))
	list2013.append(Album("Thee Oh Sees", "Floating Coffin", "http://coverartarchive.org/release/877221c2-a4fe-4c34-b89f-8d43adb31d80/front-250.jpg"))
	list2013.append(Album("Disclosure", "Settle", "http://coverartarchive.org/release-group/cefd427e-185e-4a94-a6a9-a03d8a53b60a/front-250.jpg"))
	list2013.append(Album("Eluvium", "Nightmare Ending", "https://images-na.ssl-images-amazon.com/images/I/51cxWby5TJL.jpg"))
	list2013.append(Album("Fuck Buttons", "Slow Focus", "http://coverartarchive.org/release-group/77a52eec-07c6-477a-9c9e-f0de4c473d61/front-250.jpg"))
	list2013.append(Album("Future Of The Left", "How To Stop Your Brain In An Accident", "http://coverartarchive.org/release/234bcd09-f7b7-4b9c-a427-baf839abc453/front-250.jpg"))
	list2013.append(Album("Kanye West", "Yeezus", "http://coverartarchive.org/release/44f67341-2586-4283-bc3f-cf03ae89dc35/4404841321-250.jpg"))
	list2013.append(Album("Weekend Nachos", "Still", "http://www.metalinjection.net/wp-content/uploads/2013/11/Weekend-Nachos-Still.jpg"))
	list2013.append(Album("Melt-Banana", "fetch", "http://coverartarchive.org/release-group/ebde320c-2869-423b-beed-47e1df6b459e/front-250.jpg"))
	list2013.append(Album("Buke And Gase", "General Dome", "http://coverartarchive.org/release-group/8172fb2f-4af0-4abc-ae78-1a1e58b75bb7/front-250.jpg"))
	list2013.append(Album("Jenny Hval", "Innocence Is Kinky", "http://coverartarchive.org/release-group/022cf563-579e-4655-91a0-bef34732306b/front-250.jpg"))
	list2013.append(Album("The Knife", "Shaking The Habitual", "http://coverartarchive.org/release-group/06448e12-18d8-4d52-a51f-d4c83d07ec09/front-250.jpg"))
	list2013.append(Album("Sigur Ros", "Kveikur", "http://coverartarchive.org/release-group/9fa7397e-7212-425f-8158-87c3bfb79602/front-250.jpg"))
	list2013.append(Album("Ghostpoet", "Some Say I So I Say Light", "http://coverartarchive.org/release/12513a3d-404a-4db4-93f1-7b73321807dd/4033365986-250.jpg"))

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
	list2012.append(Album("Swans","The Seer","http://ia800308.us.archive.org/30/items/mbid-31f30ecf-69df-4920-89da-7bd6d9abc3f6/mbid-31f30ecf-69df-4920-89da-7bd6d9abc3f6-10402018472_thumb500.jpg"))
	list2012.append(Album("Godspeed You! Black Emperor","'Allelujah! Don't Bend! Ascend!","http://ia902705.us.archive.org/34/items/mbid-0b6d1c29-9c37-4392-ac4f-5822933f89e6/mbid-0b6d1c29-9c37-4392-ac4f-5822933f89e6-2200016389_thumb500.jpg"))
	list2012.append(Album("Fiona Apple","The Idler Wheel Is Wiser Than the Driver of the Screw and Whipping Cords Will Serve You More Than Ropes Will Ever Do","http://ia800504.us.archive.org/2/items/mbid-04c72095-a6af-41f7-a18a-a1dd7e305620/mbid-04c72095-a6af-41f7-a18a-a1dd7e305620-1264480591_thumb500.jpg"))
	list2012.append(Album("Torche","Harmonicraft","http://ia902706.us.archive.org/33/items/mbid-c0b51d77-efa8-4849-8a24-095ac377138e/mbid-c0b51d77-efa8-4849-8a24-095ac377138e-2361027232_thumb500.jpg"))
	list2012.append(Album("Bosse-de-Nage","iii","http://ecx.images-amazon.com/images/I/512w%2Bl7j2GL.jpg"))
	list2012.append(Album("Tame Impala","Lonerism","http://ia802708.us.archive.org/31/items/mbid-340898f5-7a35-4cc0-9a06-fe06fe0137b9/mbid-340898f5-7a35-4cc0-9a06-fe06fe0137b9-10223917630_thumb500.jpg"))
	list2012.append(Album("Cloud Nothings","Attack On Memory","http://ia902601.us.archive.org/30/items/mbid-36f88c0d-9036-4ef6-83f8-bc8669c36d39/mbid-36f88c0d-9036-4ef6-83f8-bc8669c36d39-2098697244_thumb500.jpg"))
	list2012.append(Album("Grizzly Bear","Shields","http://ia802706.us.archive.org/27/items/mbid-8baedb5b-192c-4426-99ee-4c23d50550bd/mbid-8baedb5b-192c-4426-99ee-4c23d50550bd-2176498254_thumb500.jpg"))
	list2012.append(Album("Spiritualized","Sweet Heart Sweet Light","http://coverartarchive.org/release-group/9b5bf979-122c-4b5d-b73d-4c22ff193828/front.jpg"))
	list2012.append(Album("Converge","All We Love We Leave Behind","http://coverartarchive.org/release-group/86037f34-72c6-4ad9-8072-f20bb839f78d/front.jpg"))
	list2012.append(Album("Action Bronson / Party Supplies","Blue Chips","http://coverartarchive.org/release-group/04428174-ec07-40de-b317-7a2f0f8c4808/front.jpg"))
	list2012.append(Album("The Men","Open Your Heart","http://coverartarchive.org/release/2b868dc8-271a-4402-b7b3-bb72d182f54c/2098745006.jpg"))
	list2012.append(Album("Royal Thunder","CVI","http://coverartarchive.org/release-group/a9cd4fcc-5aa4-4def-a511-df31ca98b2ce/front.jpg"))
	list2012.append(Album("Wodensthrone","Curse","http://coverartarchive.org/release-group/51a46170-8e31-4268-9b8e-55f5906bae91/front.jpg"))
	list2012.append(Album("Ash Borer","Cold Of Ages","http://coverartarchive.org/release-group/5557bdd2-26bf-48e5-a3bf-988ffb35cc93/front.jpg"))
	list2012.append(Album("Alt-j","An Awesome Wave","http://coverartarchive.org/release-group/0d8562eb-7f72-427b-8a0b-984cc5ee7766/front.jpg"))
	list2012.append(Album("Burial","Kindred EP","http://coverartarchive.org/release-group/1c288979-ce2f-4e4b-90e4-845908cf7ffc/front.jpg"))
	list2012.append(Album("...And You Will Know Us By The Trail Of Dead","Lost Songs","http://coverartarchive.org/release-group/b78489e8-5d85-4b51-9f4a-c556af08361a/front.jpg"))
	list2012.append(Album("iamamiwhoami","Kin","http://coverartarchive.org/release-group/2366eec5-5b8f-47e2-a18d-5910cd0ee85a/front.jpg"))
	list2012.append(Album("The Evens","The Odds","http://cdn4.pitchfork.com/news/47837/d873864c.jpg"))
	list2012.append(Album("Circle Takes The Square","Decompositions: Volume Number One","http://coverartarchive.org/release-group/b2232a36-80ce-4116-be1e-1421dea2aaf6/front.jpg"))
	list2012.append(Album("Jack White","Blunderbuss","http://coverartarchive.org/release-group/37f48931-e5e6-488f-a531-ad2db311158d/front.jpg"))
	list2012.append(Album("Japandroids","Celebration Rock","http://coverartarchive.org/release-group/32f90db3-467a-4a31-b36b-e4b73dc0cc78/front.jpg"))
	list2012.append(Album("Pig Destroyer","Book Burner","http://coverartarchive.org/release-group/2ff27be2-de49-43e4-a5a3-6ca6452efc3d/front.jpg"))
	list2012.append(Album("High On Fire","De Vermis Mysteriis","http://coverartarchive.org/release-group/26371a98-daca-4798-8c22-8bc9dfb93b26/front.jpg"))
	list2012.append(Album("Susanne Sundfor","The Silicone Veil","http://coverartarchive.org/release-group/ecbd323b-3463-497c-b40e-f2a2c41df61f/front.jpg"))
	list2012.append(Album("The Sword","Apocryphon","http://cdn.albumoftheyear.org/album/apocryphon.jpg"))
	list2012.append(Album("The Walkmen","Heaven","http://coverartarchive.org/release/5921d6cd-d098-46f4-a69e-7205ac29bbfe/946789854.jpg"))
	list2012.append(Album("Loma Prieta","I.V.","http://coverartarchive.org/release-group/d5368fc7-4181-463e-b060-9f0ad44b3580/front.jpg"))
	list2012.append(Album("Anais Mitchell","Young Man In America","http://coverartarchive.org/release-group/06fd9495-1025-416b-866a-a214f29b3036/front.jpg"))
	list2012.append(Album("Aesop Rock","Skelethon","http://coverartarchive.org/release-group/769966a4-c76b-4935-a5c0-74147dcb5b79/front.jpg"))
	list2012.append(Album("Leech","If We Get There One Day, Would You Please Open The Gates?","http://coverartarchive.org/release-group/c9e8f50d-4734-4ef7-9193-519c3b453245/front.jpg"))
	list2012.append(Album("Pigs","You Ruin Everything","https://41.media.tumblr.com/d8deb797657e7127af9fec86c2d2e3c4/tumblr_n13hysC8p81qdix05o1_500.jpg"))
	list2012.append(Album("White Rabbits","Milk Famous","http://ecx.images-amazon.com/images/I/51tdXd%2BUnYL.jpg"))
	list2012.append(Album("Cate Le Bon","CYRK","http://ecx.images-amazon.com/images/I/61XRvSU9fzL.jpg"))
	list2012.append(Album("Kowloon Walled City","Container Ships","http://coverartarchive.org/release-group/f8ea1b69-0dbf-44cc-895e-1db5d717f115/front.jpg"))
	list2012.append(Album("Wizard Rifle","Speak Loud Say Nothing","http://www.invisibleoranges.com/wp-content/uploads/2012/03/wizardrifle_album.jpeg"))
	list2012.append(Album("Bats","The Sleep Of Reason","http://coverartarchive.org/release-group/2a4a8fda-e47f-4c95-994f-7bf8ae500f3d/front.jpg"))
	list2012.append(Album("Andrew Bird","Break It Yourself","http://coverartarchive.org/release-group/97fe2ba8-1c28-45ec-a8ba-38b7e4893e3d/front.jpg"))
	list2012.append(Album("Alexandre Desplat","Moonrise Kingdom","http://ia601606.us.archive.org/35/items/mbid-349000da-5b41-4fd3-8cc2-21082ec74eee/mbid-349000da-5b41-4fd3-8cc2-21082ec74eee-3435627137_thumb500.jpg"))

	runnersUp2012 = list()
	runnersUp2012.append(Album("Colour Haze","She Said","http://coverartarchive.org/release-group/16e8b800-1009-4b8b-af9e-ea98329d096d/front.jpg"))
	runnersUp2012.append(Album("Clams Casino","Instrumental Tape 2","http://coverartarchive.org/release-group/90712528-f590-4a6d-aba0-14f459425752/front.jpg"))
	runnersUp2012.append(Album("Dinosaur Jr.","I Bet On Sky","http://coverartarchive.org/release-group/727e7b83-4709-4398-a285-da71e38b74da/front.jpg"))
	runnersUp2012.append(Album("Grave","Endless Procession Of Souls","http://ecx.images-amazon.com/images/I/61ZPMCrp4SL.jpg"))
	runnersUp2012.append(Album("John Talabot","fin","http://coverartarchive.org/release/697082bd-a67e-453a-a63c-6696b06ac98d/2985165419.jpg"))
	runnersUp2012.append(Album("Max Richter","Recomposed by Max Richter. Vivaldi - The Four Seasons","http://coverartarchive.org/release-group/b921615e-355b-47af-a13d-6a223ead16e6/front.jpg"))
	runnersUp2012.append(Album("Screaming Females","Ugly","http://coverartarchive.org/release-group/d41c8b41-efbd-46c0-a163-1d332151d112/front.jpg"))
	runnersUp2012.append(Album("Sharon Van Etten","Tramp","http://coverartarchive.org/release-group/58eff3eb-7445-4914-b38a-068e1b3bb83e/front.jpg"))
	runnersUp2012.append(Album("Suis La Lune","Riala","http://coverartarchive.org/release-group/84069713-38e2-4ab6-81a3-925fae886ae7/front.jpg"))
	runnersUp2012.append(Album("Ty Segall / White Fence","Hair","http://coverartarchive.org/release-group/0b86bf0e-f49c-43e2-83eb-586abd54b8a4/front.jpg"))

	spreadsheet2012 = dict()
	spreadsheet2012["link"] = "https://docs.google.com/spreadsheets/d/1HVcKqtqWto57-81y_5WlLINayV0dOp8MY_B7Uo3VK0Q/edit"
	spreadsheet2012["ratingCount"] = "480"
	spreadsheet2012["averageRating"] = "6.26"

	albums2012 = dict()
	albums2012["list"] = list2012
	albums2012["runnersUp"] = runnersUp2012
	albums2012["spreadsheet"] = spreadsheet2012

	list2011 = list()
	list2011.append(Album("Giles Corey","Giles Corey","http://coverartarchive.org/release-group/a5c26b66-3f39-463a-aff4-cf859da4a0c3/front.jpg"))
	list2011.append(Album("Fleet Foxes","Helplessness Blues","http://coverartarchive.org/release-group/d569deba-8c6b-4d08-8c43-d0e5a1b8c7f3/front.jpg"))
	list2011.append(Album("Tom Waits","Bad As Me","http://coverartarchive.org/release-group/956f10e8-0c74-4010-99d3-1b60fb7e88bc/front.jpg"))
	list2011.append(Album("PJ Harvey","Let England Shake","http://vignette4.wikia.nocookie.net/lyricwiki/images/e/e5/PJ_Harvey_-_Let_England_Shake.jpg/revision/latest?cb=20110225143252"))
	list2011.append(Album("Wye Oak","Civilian","http://coverartarchive.org/release-group/6ac512b1-60b5-4c7b-a923-f2699cb3addc/front.png"))
	list2011.append(Album("Kurt Vile","Smoke Ring For My Halo","http://ecx.images-amazon.com/images/I/51y-IFqkMaL.jpg"))
	list2011.append(Album("Youth Lagoon","Year of Hibernation","http://coverartarchive.org/release-group/703b7833-1dac-4d8a-9015-e0c9d45b9764/front.jpg"))
	list2011.append(Album("Woods Of Desolation","Torn Beyond Reason","http://coverartarchive.org/release-group/2b183e9d-620d-4d58-9f6d-e5ceed497b9f/front.jpg"))
	list2011.append(Album("O'Brother","Garden Window","http://coverartarchive.org/release/b3309fa4-d178-4cbd-81d3-44f6c1aa9642/3392413535.jpg"))
	list2011.append(Album("This Will Destroy You","Tunnel Blanket","http://coverartarchive.org/release-group/932067d2-4d80-495d-a037-e9c46d8d9314/front.jpg"))
	list2011.append(Album("Altar Of Plagues","Mammal","http://coverartarchive.org/release-group/9d6aedcf-234c-446d-8978-f80d83046f89/front.jpg"))
	list2011.append(Album("Wilco","The Whole Love","http://coverartarchive.org/release-group/760f9d8c-3465-497f-9186-a63b1270d9fb/front.jpg"))
	list2011.append(Album("Fell Voices","Fell Voices","http://coverartarchive.org/release-group/7b06a50e-0ab1-421b-a57d-c67ea859af5b/front.jpg"))
	list2011.append(Album("Fucked Up","David Comes To Life","http://coverartarchive.org/release-group/31fcb4ca-5845-4673-bdcc-594fd807d046/front.jpg"))
	list2011.append(Album("Bon Iver","Bon Iver, Bon Iver","http://coverartarchive.org/release-group/2cb36662-3560-4b90-a0a5-7924ac039490/front.jpg"))
	list2011.append(Album("Colin Stetson","New History Warfare Vol. 2: Judges","http://coverartarchive.org/release-group/874ac3bc-70fc-4e90-aef2-ef2b6b8927eb/front.jpg"))
	list2011.append(Album("Grails","Deep Politics","http://coverartarchive.org/release-group/eeeb33e4-2b8f-4ea5-8116-0a4c92a91f67/front.jpg"))
	list2011.append(Album("Graveyard","Hisingen Blues","http://coverartarchive.org/release-group/b60885c0-e92d-4801-8413-0116418bccce/front.jpg"))
	list2011.append(Album("Wormrot","Dirge","http://coverartarchive.org/release-group/1ae7a0d3-cd2c-4cc6-95ba-125810117a19/front.jpg"))
	list2011.append(Album("KEN Mode","Venerable","http://ecx.images-amazon.com/images/I/519dki3RrDL.jpg"))
	list2011.append(Album("Mamiffer","Mare Decendrii","http://ecx.images-amazon.com/images/I/617h3E5Q42L.jpg"))
	list2011.append(Album("St. Vincent","Strange Mercy","http://coverartarchive.org/release-group/a9c80acf-5017-4301-8da0-2d6dfb502400/front.jpg"))
	list2011.append(Album("Subrosa","No Help For The Mighty Ones","http://coverartarchive.org/release-group/908c0d81-ba8f-48e4-aa69-ed95aae58569/front.jpg"))
	list2011.append(Album("The Black Keys","El Camino","http://coverartarchive.org/release-group/c2eed4c1-5cd9-469a-9075-b82077093967/front.jpg"))
	list2011.append(Album("The Field","Looping State Of Mind","http://coverartarchive.org/release-group/6745fa25-3fbe-4c76-b29b-83ed5dea788f/front.jpg"))
	list2011.append(Album("Cave In","White Silence","http://coverartarchive.org/release-group/5981684e-a3a6-4d17-9390-1cc2670beff6/front.jpg"))
	list2011.append(Album("Tombs","Path Of Totality","http://ecx.images-amazon.com/images/I/61NRRmH%2B0DL.jpg"))
	list2011.append(Album("Fuck The Facts","Die Miserable","http://coverartarchive.org/release-group/62005bd4-f866-468c-a80b-83549ef32b75/front.jpg"))
	list2011.append(Album("Mastodon","The Hunter","http://coverartarchive.org/release-group/3c73bc27-4567-4957-8cfb-929d79b3a6ce/front.jpg"))
	list2011.append(Album("Trap Them","Darker Handcraft","http://www.brooklynvegan.com/img/metal/various/Trap_Them_-_Darker_Handcraft_artwork.jpg"))
	list2011.append(Album("*shels","Plains Of The Purple Buffalo","http://coverartarchive.org/release-group/3768f323-10a6-460e-8d73-914f594b81bf/front.jpg"))
	list2011.append(Album("Tim Hecker","Ravedeath,1972","http://coverartarchive.org/release-group/b55c9544-ba14-436f-a97e-2157b10d540d/front.jpg"))
	list2011.append(Album("The Roots","Undun","http://coverartarchive.org/release-group/3d5c691e-61bd-4235-999b-31ebea927227/front.jpg"))
	list2011.append(Album("Cormorant","Dwellings","http://www.invisibleoranges.com/wp-content/uploads/2012/01/cormorant_dwellings.jpg"))
	list2011.append(Album("Corrupted","Garten Der Unbewusstheit","http://coverartarchive.org/release-group/8d440a0f-8731-4736-86ef-36cd9bab3bd0/front.jpg"))
	list2011.append(Album("M83","Hurry Up We're Dreaming","http://coverartarchive.org/release-group/5f898a60-acc5-48fc-a11b-2926084c0924/front.jpg"))
	list2011.append(Album("Widowspeak","Widowspeak","http://ia600403.us.archive.org/18/items/mbid-ed1d9bee-fdaf-4a26-bc5d-f3c7a25780b9/mbid-ed1d9bee-fdaf-4a26-bc5d-f3c7a25780b9-6426811654_thumb500.jpg"))
	list2011.append(Album("Terra Tenebrosa","The Tunnels","http://coverartarchive.org/release-group/d05b7693-e00b-4a66-abad-accad6ea80fe/front.jpg"))
	list2011.append(Album("Trent Reznor & Atticus Ross","The Girl With The Dragon Tattoo","http://coverartarchive.org/release-group/5bae78a4-6a78-42bb-9272-ea1252fec6fd/front.jpg"))
	list2011.append(Album("Battles","Gloss Drop","http://coverartarchive.org/release-group/6016a44b-2b1b-483f-bd3f-e67d2ac534c2/front.jpg"))
	
	runnersUp2011 = list()
	runnersUp2011.append(Album("Disma","Towards The Megalith","http://coverartarchive.org/release-group/6e2a41a7-0d99-46c0-bab1-2fde73e72d0c/front.jpg"))
	runnersUp2011.append(Album("Diskinesia","Dalla Nascita","https://f1.bcbits.com/img/a2410845608_10.jpg"))
	runnersUp2011.append(Album("Feist","Metals","http://ecx.images-amazon.com/images/I/51jgOu9IjRL.jpg"))
	runnersUp2011.append(Album("La Dispute","Wildlife","http://coverartarchive.org/release-group/56b3b007-8332-4a42-b074-2d8b04cdadf1/front.jpg"))
	runnersUp2011.append(Album("Matana Roberts","Coin Coin Chapter One: Gens De Couleur Libres","http://ecx.images-amazon.com/images/I/61ZMrQnbBqL.jpg"))
	runnersUp2011.append(Album("The Men","Leave Home","http://coverartarchive.org/release-group/7c8ff532-b512-4c61-9510-e368b5bb81bf/front.jpg"))
	runnersUp2011.append(Album("Nicolas Jaar","Space Is Only Noise","http://coverartarchive.org/release-group/0fa5e3d1-22b1-4232-adca-0ec05c4c69e7/front.jpg"))
	runnersUp2011.append(Album("Noel Gallagher's High Flying Birds","Noel Gallagher's High Flying Birds","http://ecx.images-amazon.com/images/I/51sbfC6U3JL.jpg"))
	runnersUp2011.append(Album("Slow Club","Paradise","http://ecx.images-amazon.com/images/I/51lDcrzhD3L.jpg"))
	runnersUp2011.append(Album("Solstafir","Svartir Sandarr","http://coverartarchive.org/release-group/3d46b486-44bc-4765-bb0d-40a74e630d32/front.jpg"))
	runnersUp2011.append(Album("Richard Buckner","Our Blood","http://ecx.images-amazon.com/images/I/51lidEERF4L.jpg"))
	runnersUp2011.append(Album("Rome","Die Aesthetik der Herrschaftsfreiheit","http://ecx.images-amazon.com/images/I/41S9qHG86NL._SY300_.jpg"))
	runnersUp2011.append(Album("Russian Circles","Empros","http://coverartarchive.org/release-group/5dc00b2d-4691-4d35-b137-ba646514f096/front.jpg"))	
	runnersUp2011.append(Album("Thou","The Archer & The Owle","http://coverartarchive.org/release-group/c333dd88-44e7-488c-91a6-e4cca94def10/front.jpg"))
	runnersUp2011.append(Album("Washed Out","Within And Without","http://coverartarchive.org/release-group/df595313-7291-446d-9a8f-0d15068e474a/front.jpg"))



	spreadsheet2011 = dict()
	spreadsheet2011["link"] = "https://docs.google.com/spreadsheets/d/1dMrtTnsVO0vlNwcrfBgWhH25qvP3aThXWBM-EL8PGD4/edit"
	spreadsheet2011["ratingCount"] = "354"
	spreadsheet2011["averageRating"] = "6.95"

	albums2011 = dict()
	albums2011["list"] = list2011
	albums2011["runnersUp"] = runnersUp2011
	albums2011["spreadsheet"] = spreadsheet2011


	listData = dict()
	listData["2014"] = albums2014
	listData["2013"] = albums2013
	listData["2012"] = albums2012
	listData["2011"] = albums2011
	logging.info(albums2014)
	logging.info(listData)

	return listData


class Album:
	def __init__(self, artistName, albumName, imgUrl):
		self.artistName = artistName
		self.albumName = albumName
		self.imgUrl = imgUrl

	# def __repr__(self):
	# 	return "Name: [%s], Release [%s], Img [%s]" % (self.artistName, self.albumName, self.albumImage)

