
#Fix NULLs for country values


# astro_db.loc[astro_db['astronaut_name'] == "Sergey V. Prokopyev", 'country'] = "Russia"
# astro_db.loc[astro_db['astronaut_name'] == "Serena M. Auñón-Chancellor", 'country'] = "United States of America"


bio_data['full_names'] = bio_data['full_names'].str.replace('Robert Kimbrough','Robert S. Kimbrough')
bio_data['full_names'] = bio_data['full_names'].str.replace('Michael Adams','Michael J. Adams')
bio_data['full_names'] = bio_data['full_names'].str.replace('Neil Armstrong','Neil A. Armstrong')
bio_data['full_names'] = bio_data['full_names'].str.replace('K. McArthur','K. Megan McArthur')
bio_data['full_names'] = bio_data['full_names'].str.replace('Sian  Proctor','Dr. Sian Proctor')
bio_data['full_names'] = bio_data['full_names'].str.replace('John McKay','John B. McKay')
bio_data['full_names'] = bio_data['full_names'].str.replace('Tang Hong','Tang Hongbo')
bio_data['full_names'] = bio_data['full_names'].str.replace('James Lovell','James A. Lovell Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Thomas Stafford','Thomas P. Stafford')
bio_data['full_names'] = bio_data['full_names'].str.replace('John Young','John W. Young')


bio_data['full_names'] = bio_data['full_names'].str.replace('Eugene Cernan','Eugene A. Cernan')
bio_data['full_names'] = bio_data['full_names'].str.replace('Charles Conrad','Charles Conrad Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Gordon','Richard F. Gordon Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Alan Bean','Alan L. Bean')
bio_data['full_names'] = bio_data['full_names'].str.replace('John Swigert','John L. Swigert Jr.')

bio_data['full_names'] = bio_data['full_names'].str.replace('Fred Haise','Fred W. Haise Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Vladimir Titov','Vladimir G. Titov')
bio_data['full_names'] = bio_data['full_names'].str.replace('Robert Crippen','Robert L. Crippen')
bio_data['full_names'] = bio_data['full_names'].str.replace('Jon McBride','Jon A. McBride')
bio_data['full_names'] = bio_data['full_names'].str.replace('Kathryn Sullivan','Kathryn D. Sullivan')
bio_data['full_names'] = bio_data['full_names'].str.replace('David Leestma','David C. Leestma')
bio_data['full_names'] = bio_data['full_names'].str.replace('Paul Scully-Power','Paul D. Scully-Power')
bio_data['full_names'] = bio_data['full_names'].str.replace('Joe Engle','Joe H. Engle')
bio_data['full_names'] = bio_data['full_names'].str.replace('Virgil Grissom','Virgil I. Grissom')
bio_data['full_names'] = bio_data['full_names'].str.replace('Joseph Walker','Joseph A. Walker')
bio_data['full_names'] = bio_data['full_names'].str.replace('James McDivitt','James A. McDivitt')
bio_data['full_names'] = bio_data['full_names'].str.replace('Edward White','Edward H. White II')
bio_data['full_names'] = bio_data['full_names'].str.replace('L. Cooper','L. Gordon Cooper Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Walter Schirra','Walter M. Schirra Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('William Anders','William A. Anders')




bio_data['full_names'] = bio_data['full_names'].str.replace('Oleg Makarov','Oleg G. Makarov')
bio_data['full_names'] = bio_data['full_names'].str.replace('Franklin Musgrave','F. Story Musgrave')
bio_data['full_names'] = bio_data['full_names'].str.replace('Kathryn Thornton','Kathryn C. Thornton')
bio_data['full_names'] = bio_data['full_names'].str.replace('Robert Cabana','Robert D. Cabana')
bio_data['full_names'] = bio_data['full_names'].str.replace('David Wolf','David A. Wolf')
bio_data['full_names'] = bio_data['full_names'].str.replace('Kent Rominger','Kent V. Rominger')
bio_data['full_names'] = bio_data['full_names'].str.replace('Frederick Sturckow','Frederick W. Sturckow')
bio_data['full_names'] = bio_data['full_names'].str.replace('Henry Hartsfield','Henry W. Hartsfield Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Daniel Brandenstein','Daniel C. Brandenstein')
bio_data['full_names'] = bio_data['full_names'].str.replace('Guion Bluford','Guion S. Bluford Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Steven Hawley','Steven A. Hawley')
bio_data['full_names'] = bio_data['full_names'].str.replace('Frederick Gregory','Frederick D. Gregory')
bio_data['full_names'] = bio_data['full_names'].str.replace('John Creighton','John O. Creighton')
bio_data['full_names'] = bio_data['full_names'].str.replace('Steven Nagel','Steven R. Nagel')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Covey','Richard O. Covey')
bio_data['full_names'] = bio_data['full_names'].str.replace('Aleksandr Volkov','Aleksandr A. Volkov')
bio_data['full_names'] = bio_data['full_names'].str.replace('James Buchli','James F. Buchli')
bio_data['full_names'] = bio_data['full_names'].str.replace('Thomas Akers','Thomas D. Akers')
bio_data['full_names'] = bio_data['full_names'].str.replace('Nancy Currie-Gregg','Nancy J. Currie-Gregg')
bio_data['full_names'] = bio_data['full_names'].str.replace('John Blaha','John E. Blaha')
bio_data['full_names'] = bio_data['full_names'].str.replace('Janice Voss','Janice E. Voss')
bio_data['full_names'] = bio_data['full_names'].str.replace('Kenneth Bowersox','Kenneth D. Bowersox')
bio_data['full_names'] = bio_data['full_names'].str.replace('Scott Parazynski','Scott E. Parazynski')
bio_data['full_names'] = bio_data['full_names'].str.replace('Scott Altman','Scott D. Altman')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Linnehan','Richard M. Linnehan')
bio_data['full_names'] = bio_data['full_names'].str.replace('Doug Hurley','Douglas G. Hurley')






