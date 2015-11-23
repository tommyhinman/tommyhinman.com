import logging

def getAlbumListData():
	albums2014 = list()
	albums2014.append(Album("Swans", "To Be Kind", "http://coverartarchive.org/release-group/d2df1a2d-4da1-40a3-a825-5674ce117579/front-500.jpg"))
	albums2014.append(Album("Iceage","Plowing Into The Field Of Love","http://coverartarchive.org/release-group/5792bd69-7664-4a23-87aa-5f43c9b48338/front-500.jpg"))
	albums2014.append(Album("Sun Kil Moon", "Benji", "http://coverartarchive.org/release-group/9e14617c-3842-4d5f-bef4-16b38f2c9f4e/front-500.jpg"))
	albums2014.append(Album("Ought","More Than Any Other Day","http://coverartarchive.org/release/1f459335-11f6-441e-a07b-4ff102352ac2/6831251404-500.jpg"))
	albums2014.append(Album("Thee Silver Mt. Zion Memorial Orchestra","Fuck Off Get Free We Pour Light Onto Everything","http://coverartarchive.org/release-group/0c6dca7d-e1bb-4dfd-aaf5-35c60bb910cd/front-500.jpg"))
	albums2014.append(Album("Angel Olsen","Burn Your Fire For No Witness","http://coverartarchive.org/release-group/8cb480c5-404f-4f65-ad88-ba77e19ef33c/front-500.jpg"))
	albums2014.append(Album("Cloud Nothings","Here And Nowhere Else","http://coverartarchive.org/release-group/f8255f7a-5669-4f1d-92e8-7188fa284017/front-500.jpg"))
	albums2014.append(Album("The Austerity Program","Beyond Calculation","https://40.media.tumblr.com/4569c9d7993221d5299e71f034096be9/tumblr_n7l2158ORW1qasfv5o3_500.jpg"))
	albums2014.append(Album("Old Man Gloom","The Ape of God","http://ecx.images-amazon.com/images/I/614yxe1RvHL.jpg"))
	albums2014.append(Album("White Lung","Deep Fantasy","http://coverartarchive.org/release-group/786fe66b-ab44-4b6c-9cf1-a4d14662f2f0/front-500.jpg"))
	albums2014.append(Album("Together Pangea","Badillac","http://coverartarchive.org/release-group/5e947f97-ebc7-4e51-932d-41b37cabaa51/front-500.jpg"))
	albums2014.append(Album("The War On Drugs","Lost In The Dream","http://coverartarchive.org/release-group/943b191f-616f-4091-8516-0979987b5eef/front-500.jpg"))
	albums2014.append(Album("La Dispute","Rooms Of The House","http://coverartarchive.org/release-group/8dc09bff-dd15-4dc7-b195-8814224a9325/front-500.jpg"))
	albums2014.append(Album("Thou","Heathen","http://coverartarchive.org/release/c13dc4ab-ce79-4a64-ba08-79b87d966095/7796754563-500.jpg"))
	albums2014.append(Album("Sharon Van Etten","Are We There","http://coverartarchive.org/release-group/60cbb40c-1db0-4e5b-81a7-b693a67dff0a/front-500.jpg"))
	albums2014.append(Album("Ty Segall","Manipulator","http://coverartarchive.org/release-group/955fba0f-6aab-407a-b6cf-cce8b4f79717/front-500.jpg"))
	albums2014.append(Album("Young Widows","Easy Pain","http://coverartarchive.org/release-group/3b2f53a2-d2de-4a9a-9e68-9f0f47d1e818/front-500.jpg"))
	albums2014.append(Album("Shellac","Dude Incredible","http://coverartarchive.org/release-group/93eddd2b-7ee2-4489-85f7-f52ce9e60658/front-500.jpg"))
	albums2014.append(Album("Survival Knife","Loose Power","http://coverartarchive.org/release-group/5783231b-50e7-47f4-b15b-2798ad63124d/front-500.jpg"))
	albums2014.append(Album("Death From Above 1979","The Physical World","http://coverartarchive.org/release-group/c57c63e1-b367-489a-a75f-ddd711e91174/front-500.jpg"))
	albums2014.append(Album("Krieg","Transient","http://www.nocleansinging.com/wp-content/uploads/2014/08/Krieg-Transient.jpg"))
	albums2014.append(Album("Have A Nice Life","The Unnatural World","http://ffhdbrhd7sg2o09k.zippykid.netdna-cdn.com/wp-content/uploads/2014/02/fr39coverart.jpg"))
	albums2014.append(Album("Helms Alee","Sleepwalking Sailors","http://coverartarchive.org/release-group/456243fe-c125-477c-8841-4ba46e26b1dd/front-500.jpg"))
	albums2014.append(Album("Kevin Morby","Still Life","http://coverartarchive.org/release-group/0a9ac7e0-980e-473d-afee-f17e3171f93b/front-500.jpg"))
	albums2014.append(Album("Cymbals Eat Guitars","LOSE","http://coverartarchive.org/release-group/0f8a2660-78ec-4863-add5-9cf5ad0b14e4/front-500.jpg"))
	albums2014.append(Album("Run The Jewels","RTJ2","http://coverartarchive.org/release-group/581d7ac8-8f1d-4d4a-a224-de9c9cd76b39/front-500.jpg"))
	albums2014.append(Album("A Sunny Day In Glasgow","Sea When Absent","http://coverartarchive.org/release-group/cc514c1c-1b6c-476d-bc93-d96ef0e21757/front-500.jpg"))
	albums2014.append(Album("A Winged Victory For The Sullen","Atmos","http://coverartarchive.org/release-group/7bc3d477-b550-40b0-abdb-febe66b92290/front-500.jpg"))
	albums2014.append(Album("Dope Body","Lifer","https://i.ytimg.com/vi/BtaOjS04smU/maxresdefault.jpg"))
	albums2014.append(Album("Goat","Commune","https://ia902302.us.archive.org/2/items/mbid-73159b10-18ef-4dd0-91dc-3facb6ecb6df/mbid-73159b10-18ef-4dd0-91dc-3facb6ecb6df-8309930145_thumb500.jpg"))



	albums2013 = list()
	albums2013.append(Album("Jon Hopkins", "Immunity", "http://ia801801.us.archive.org/3/items/mbid-9b93c88b-b939-4206-af30-b3a3e7f1ab8d/mbid-9b93c88b-b939-4206-af30-b3a3e7f1ab8d-4299705401_thumb500.jpg"))
	albums2013.append(Album("Kurt Vile", "Wakin on a Pretty Daze", "https://ia801702.us.archive.org/2/items/mbid-b62e3ec7-d6bb-43c6-8eb8-30d958d109d0/mbid-b62e3ec7-d6bb-43c6-8eb8-30d958d109d0-3846880817_thumb500.jpg"))
	albums2013.append(Album("Nils Frahm", "Spaces", "http://coverartarchive.org/release/6f9f69af-f0d6-40d8-8f33-de7a3f0ca052/5854196919-500.jpg"))
	albums2013.append(Album("Altar Of Plagues", "Teethed Glory And Injury", "http://coverartarchive.org/release-group/6d809bf6-4d98-4509-aa3b-587dcd82d081/front-500.jpg"))
	albums2013.append(Album("Darkside", "Psychic", "http://coverartarchive.org/release/873f8153-2758-4f33-8399-5d00e4b9370e/front-500.jpg"))
	albums2013.append(Album("Iceage", "You're Nothing", "http://coverartarchive.org/release-group/01357463-b63c-4a6b-ade1-8b5f4eb55b96/front-500.jpg"))
	albums2013.append(Album("Cult Of Luna", "Vertikal", "http://coverartarchive.org/release/ca88ef67-66c1-4c4c-ac3e-66d178d575d6/3169895120-500.jpg"))
	albums2013.append(Album("The National", "Trouble Will Find Me", "http://coverartarchive.org/release-group/a5a2875f-41cb-4c48-9a72-e845d224db96/front-500.jpg"))
	albums2013.append(Album("Widowspeak", "Almanac", "http://coverartarchive.org/release-group/b3bb63c1-4b8c-4a19-8227-155ef324ff48/front-500.jpg"))
	albums2013.append(Album("Volcano Choir", "Repave", "http://coverartarchive.org/release-group/82686fd2-265e-4220-aac7-5c93dd395608/front-500.jpg"))
	albums2013.append(Album("Deafheaven", "Sunbather", "http://coverartarchive.org/release-group/8a061d0e-fa0c-4571-91ff-8bc3911b6428/front-500.jpg"))
	albums2013.append(Album("Vampire Weekend", "Modern Vampires Of The City", "http://coverartarchive.org/release-group/eb143c5a-9a85-4bce-a78c-f7faf72c0169/front-500.jpg"))
	albums2013.append(Album("Tim Hecker", "Virgins", "http://coverartarchive.org/release-group/8121eda6-f17d-4eaa-bd44-598828df0bc9/front-500.jpg"))
	albums2013.append(Album("Year Of No Light", "Tocsin", "http://coverartarchive.org/release-group/26b8d47c-b44c-4ade-ade6-1feb1ab230ee/front-500.jpg"))
	albums2013.append(Album("Chelsea Wolfe", "Pain Is Beauty", "http://coverartarchive.org/release-group/50ef8504-86ca-4f2f-b46f-006458e416f3/front-500.jpg"))
	albums2013.append(Album("Queens Of The Stone Age", "Like Clockwork", "http://coverartarchive.org/release-group/c92f73ee-527f-42ed-a556-fd615941e214/front-500.jpg"))
	albums2013.append(Album("Subrosa", "More Constant Than The Gods", "http://coverartarchive.org/release-group/fd11cada-e35a-4eb7-9ee9-9e024f404ee8/front-500.jpg"))
	albums2013.append(Album("Nick Cave And The Bad Seeds", "Push The Sky Away", "http://coverartarchive.org/release-group/ae8faaeb-9134-400d-819b-773e20a7d4e4/front-500.jpg"))
	albums2013.append(Album("Gorguts", "Colored Sands", "http://coverartarchive.org/release-group/6153aa16-7ec4-483d-9592-29039fc27f25/front-500.jpg"))
	albums2013.append(Album("Young Fathers", "Tape Two", "http://coverartarchive.org/release-group/8ec3c767-a998-4e09-bf62-705106abea32/front-500.jpg"))
	albums2013.append(Album("Waxahatchee", "Cerulean Salt", "http://coverartarchive.org/release-group/78bf1ed3-3d6c-48a7-a651-7489631ac9fd/front-500.jpg"))
	albums2013.append(Album("Boards Of Canada", "Tomorrow's Harvest", "http://coverartarchive.org/release/d1f52538-291c-45a3-80a1-ac601f84ab87/front-500.jpg"))
	albums2013.append(Album("Roy Harper", "Man And Myth", "http://ecx.images-amazon.com/images/I/819kzrtOplL._SL1397_.jpg"))
	albums2013.append(Album("Oneohtrix Point Never", "R Plus Seven", "http://coverartarchive.org/release/10cc746f-786c-4307-b8de-92a687489cb4/front-250.jpg"))
	albums2013.append(Album("Deerhunter", "Monomania", "http://coverartarchive.org/release-group/ddee6c28-e113-4437-8dcf-bb412ec5c9d4/front-250.jpg"))
	albums2013.append(Album("The Drones", "I See Seaweed", "http://coverartarchive.org/release-group/8be5799b-6c5d-48a6-8f88-6472c33d54bd/front-250.jpg"))
	albums2013.append(Album("Armand Hammer", "Race Music", "http://coverartarchive.org/release-group/8bb34c00-1cc6-4b2b-92a4-e4d6c536fcc1/front-250.jpg"))
	albums2013.append(Album("Thee Oh Sees", "Floating Coffin", "http://coverartarchive.org/release/877221c2-a4fe-4c34-b89f-8d43adb31d80/front-250.jpg"))
	albums2013.append(Album("Disclosure", "Settle", "http://coverartarchive.org/release-group/cefd427e-185e-4a94-a6a9-a03d8a53b60a/front-250.jpg"))
	albums2013.append(Album("Eluvium", "Nightmare Ending", "https://images-na.ssl-images-amazon.com/images/I/51cxWby5TJL.jpg"))
	albums2013.append(Album("Fuck Buttons", "Slow Focus", "http://coverartarchive.org/release-group/77a52eec-07c6-477a-9c9e-f0de4c473d61/front-250.jpg"))
	albums2013.append(Album("Future Of The Left", "How To Stop Your Brain In An Accident", "http://coverartarchive.org/release/234bcd09-f7b7-4b9c-a427-baf839abc453/front-250.jpg"))
	albums2013.append(Album("Kanye West", "Yeezus", "http://coverartarchive.org/release/44f67341-2586-4283-bc3f-cf03ae89dc35/4404841321-250.jpg"))
	albums2013.append(Album("Weekend Nachos", "Still", "http://www.metalinjection.net/wp-content/uploads/2013/11/Weekend-Nachos-Still.jpg"))
	albums2013.append(Album("Melt-Banana", "fetch", "http://coverartarchive.org/release-group/ebde320c-2869-423b-beed-47e1df6b459e/front-250.jpg"))
	albums2013.append(Album("Buke And Gase", "General Dome", "http://coverartarchive.org/release-group/8172fb2f-4af0-4abc-ae78-1a1e58b75bb7/front-250.jpg"))
	albums2013.append(Album("Jenny Hval", "Innocence Is Kinky", "http://coverartarchive.org/release-group/022cf563-579e-4655-91a0-bef34732306b/front-250.jpg"))
	albums2013.append(Album("The Knife", "Shaking The Habitual", "http://coverartarchive.org/release-group/06448e12-18d8-4d52-a51f-d4c83d07ec09/front-250.jpg"))
	albums2013.append(Album("Sigur Ros", "Kveikur", "http://coverartarchive.org/release-group/9fa7397e-7212-425f-8158-87c3bfb79602/front-250.jpg"))
	albums2013.append(Album("Ghostpoet", "Some Say I So I Say Light", "http://coverartarchive.org/release/12513a3d-404a-4db4-93f1-7b73321807dd/4033365986-250.jpg"))


	listData = dict()
	listData["2014"] = albums2014
	listData["2013"] = albums2013
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

