import csv, os

with open("100MostStreamedSongs.csv") as file: 
  reader = csv.DictReader(file) 

  for row in reader:
    Folders = os.listdir()
    if row['Artist(s)'] not in Folders:
      os.mkdir(row["Artist(s)"])
    Folder = row["Artist(s)"] + "/"
    FilePath = os.path.join(Folder,row["Song"])
    f = open(FilePath, "w")
    f.close()