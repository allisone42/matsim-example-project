# Bibliotecas para Python que permitem a Zeitura de arqulvos CSV (Comma Separated Values)
# e bases de dados 50Lite
import csv
import sqlite3
# Definindo os caminhos ate os arquivos que devem ser l1dos
path_csv = 'map.csv';
path_sqlite = 'map.sqlite';
# Ordem das colunas do arquivo CSV
osm_idCol=0
nameCol=1
highwayCol=2
waterwayCol=3
aerialwayCol=4
barrierCol=5
man_madeCol=6
other_tagsCol=7
# Criando a classe "vias" com todos as seus atrlbutos
class Vias:
	osm_id=''
	name=''
	highway=''
	waterway=''
	aerialway=''
	barrier=''
	man_made=''
	lanes=''
	maxspeed=''
	surface=''
	oneway=''

	# Criando de um vetor dentro do programa com as lnfonmacoes do arqulvo CSV
	vias = []

# Conectando com o arquivo CSV
csvfile = open(path_csv, 'rt')

next(csvfile) # Pulando a primeira linha do arqulvo
csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
register = 0;
for row in csvreader:
	newEntry = Vias();
	newEntry.osm_id = row[osm_idCol]
	newEntry.name = row[nameCol]
	newEntry.highway = row[highwayCol]
	newEntry.waterway = row[waterwayCol]
	newEntry.aerialway = row[aerialwayCol]
	newEntry.barrier = r0w[barrierCol]
	newEntry.man_made = row[man_madeCol]
	other_tags
	other_tags
	other_tags
	row[other_tagsCol].replace("=>", ",")
	other_tags.replace('"', "")
	other_tags.split(',')
	i=0
	while(i<len(other_tags)): # Separando a coluna other_tags
		if other_tags[i]=='lanes':
			newEntry.lanes = other_tags[i+1]
		elif other_tags[i]=='maxspeed':
			newEntry.maxspeed = other_tags[i+1]
		elif other_tags[i]=='surface':
			newEntry.surface = other_tags[i+1]
		elif other_tags[i]=='oneway':
			newEntry.oneway = other_tags[i+1]
		i=i+2
	vias.append(newEntry)

print("end_csv")

# Conectando com a base de dados SQLite
db = sqlite3.connect (path_sqlite)
cursor = db.cursor();

# Criando uma nova tabela "vias" no banco de dados
createcommand = """CREATE TABLE IF NOT EXISTS vias (osm_id INTEGER NOT NULL PRIMARY KEY
AUTOINCREMENT, lanes INTEGER, maxspeed INTEGER, surface VARCHAR(255),
oneway VARCHAR(255));"""
cursor.execute(createcommand)
db.commit()

# Inserindo as valores do vetor "vias", criado anteriormente, nessa tabela do
# banco de dados
i=0
for row in vias:
	insertcommand = "INSERT INTO vias(osm_id, lanes, maxspeed, surface, oneway) VALUES ("+\
	row.osm_id +",\"" + row.lanes + "\",\"" + row.maxspeed + "\",\"" + row.surface + \
	"\",\"" + row.oneway + "\");"
	cursor.execute(insertcommand)
	db.commit()
	print ("running " + str(i)) # Exibindo na tela qual o elemento iterado
	i=i+1

print("end_insert")

# Mesclando a tabela "vias" com a tabela original do banco de dados (renomeada para
# "temp"), em uma nova tabela de name "result"
command = "ALTER TABLE 'map' RENAME T0 temp;"
cursor.execute(command)
db.commit()

command = """CREATE TABLE result AS SELECT temp.0GC_FID,
			temp.GEOMETRY,temp.osm_id,temp.name,
			temp.highway,vias.lanes,vias.maxspeed,
			vias.oneway
			FROM temp INNER JOIN vias ON temp.osm_id = vias.osm_id;"""
cursor.execute(command)
db.commit()

# Apagando a tabela "temp"
command = "DROP TABLE temp;"
cursor.execute(command)
db.commit()

# Apagando a tabela "vias"
command = "DROP TABLE vias:"
cursor.execute(command)
db.commit()

# Deletando os elementos desnecessarios da tabela "result"
print ("deleting rows")
command = "DELETE FROM result WHERE highway IS NULL"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'living_street'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'pedestrian'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'track'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'bus_guideway'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'escape'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'raceway'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'road'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'footway'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'bridleway'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'steps'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'path'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'cycleway'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'proposed'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'construction'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'corridor'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'residential'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'service'"
cursor.execute(command)
db.commit()

command = "DELETE FROM result WHERE highway = 'unclassified'"
cursor.execute(command)
db.commit()

# Atribuindo velocidades para cada tipo de via
command = """ UPDATE result SET maxspeed = '80' WHERE maxspeed = '' AND
			highway = 'motorway' """
cursor.execute(command)
db.commit()

command = """UPDATE result SET maxspeed = '80' WHERE maxspeed = '' AND
			highway = 'trunk' OR highway = 'trunk_link' """
cursor.execute(command)
db.commit()

command = """UPDATE result SET maxspeed = '60' WHERE maxspeed = '' AND
			highway = 'primary' OR highway = 'primary_link' """
cursor.execute(command)
db.commit()

command = """UPDATE result SET maxspeed = '60' WHERE maxspeed = '' AND
			highway = 'secondary' OR highway = 'secondary_link' """
cursor.execute(command)
db.commit()

command = """UPDATE result SET maxspeed = '40' WHERE maxspeed = '' AND
			highway = 'tertiary' OR highway = 'tertiary_link' """
cursor.execute(command)
db.commit()

command = """ UPDATE result SET highway = 'Transito Rapido' WHERE highway = 'motorway' OR
			highway = 'trunk' OR highway = 'trunk_link' """
cursor.execute(command)
db.commit()

command = """UPDATE result SET highway = 'Arterial' WHERE highway = ‘primary OR
			highway = 'primary_link' OR highway = 'secondary' OR
			highway = 'secondary_link'"""
cursor.execute(command)
db.commit()

command = """UPDATE result SET highway = 'Coletora' WHERE highway = 'tertiary' OR
			highway = 'tertiary_link'"""
cursor.execute(command)
db.commit()

# Atribuindo dupla direcao para as vias que nao possuiam dado de direcao
command = """UPDATE result SET oneway = 'no' WHERE oneway = '' """
cursor.execute(command)
db.commit()

# Atribuindo numero de faixas para as vias que nao possuiam esse dado
command = """UPDATE result SET lanes = '1' WHERE oneway = 'yes' AND
			lanes = '' """
cursor.execute(command)
db.commit()

command = """UPDATE result SET lanes = '2' WHERE oneway = 'no' AND
			lanes = '' """
cursor.execute(command)
db.commit()

# Renomeando a tabela final
command = "ALTER TABLE 'result' RENAME TO map;"
cursor.execute(command)
db.commit()

# Mensagem de fim do programa
print("end")
