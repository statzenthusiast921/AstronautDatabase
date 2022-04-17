
#Fix:
#1.) Names that were spelled differently
#2.) Inclusion or Exclusion of Middle initial
#3.) Special characters that got messed up (eg: accents)



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


bio_data['full_names'] = bio_data['full_names'].str.replace('David Scott','David R. Scott')
bio_data['full_names'] = bio_data['full_names'].str.replace('Jack Lousma','Jack R. Lousma')
bio_data['full_names'] = bio_data['full_names'].str.replace('Vance Brand','Vance D. Brand')
bio_data['full_names'] = bio_data['full_names'].str.replace('Yury Malyshev','Yury V. Malyshev')
bio_data['full_names'] = bio_data['full_names'].str.replace('C. Fullerton','C. Gordon Fullerton')
bio_data['full_names'] = bio_data['full_names'].str.replace('Robert Overmyer','Robert F. Overmyer')
bio_data['full_names'] = bio_data['full_names'].str.replace('Joseph Allen','Joseph P. Allen')
bio_data['full_names'] = bio_data['full_names'].str.replace('Frederick Hauck','Frederick H. Hauck')
bio_data['full_names'] = bio_data['full_names'].str.replace('John Fabian','John M. Fabian')
bio_data['full_names'] = bio_data['full_names'].str.replace('Norman Thagard','Norman E. Thagard')
bio_data['full_names'] = bio_data['full_names'].str.replace('Dale Gardner','Dale A. Gardner')
bio_data['full_names'] = bio_data['full_names'].str.replace('William Thornton','William E. Thornton')
bio_data['full_names'] = bio_data['full_names'].str.replace('Francis Scobee','Francis R. Scobee')
bio_data['full_names'] = bio_data['full_names'].str.replace('James van Hoften','James D. van Hoften')
bio_data['full_names'] = bio_data['full_names'].str.replace('George Nelson','George D. Nelson')
bio_data['full_names'] = bio_data['full_names'].str.replace('Michael Coats','Michael L. Coats')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Mullane','Richard M. Mullane')
bio_data['full_names'] = bio_data['full_names'].str.replace('Judith Resnik','Judith A. Resnik')
bio_data['full_names'] = bio_data['full_names'].str.replace('Charles Walker','Charles D. Walker')
bio_data['full_names'] = bio_data['full_names'].str.replace('David Walker','David M. Walker')
bio_data['full_names'] = bio_data['full_names'].str.replace('Margaret Seddon','Margaret R. Seddon')
bio_data['full_names'] = bio_data['full_names'].str.replace('Jeffrey Hoffman','Jeffrey A. Hoffman')


bio_data['full_names'] = bio_data['full_names'].str.replace('Shannon Lucid','Shannon W. Lucid')
bio_data['full_names'] = bio_data['full_names'].str.replace('Bonnie Dunbar','Bonnie J. Dunbar')
bio_data['full_names'] = bio_data['full_names'].str.replace('Robert Gibson','Robert L. Gibson')
bio_data['full_names'] = bio_data['full_names'].str.replace('Robert Springer','Robert C. Springer')
bio_data['full_names'] = bio_data['full_names'].str.replace('Pierre Thuot','Pierre J. Thuot')
bio_data['full_names'] = bio_data['full_names'].str.replace('Bruce Melnick','Bruce E. Melnick')
bio_data['full_names'] = bio_data['full_names'].str.replace('Frank Culbertson','Frank L. Culbertson Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Charles Gemar','Charles D. Gemar')
bio_data['full_names'] = bio_data['full_names'].str.replace('Terence Henricks','Terence T. Henricks')
bio_data['full_names'] = bio_data['full_names'].str.replace('James Voss','James S. Voss')
bio_data['full_names'] = bio_data['full_names'].str.replace('Kevin Chilton','Kevin P. Chilton')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Hieb','Richard J. Hieb')
bio_data['full_names'] = bio_data['full_names'].str.replace('Curtis Brown','Curtis L. Brown Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Mark Lee','Mark C. Lee')
bio_data['full_names'] = bio_data['full_names'].str.replace('Jerome Apt','Jerome Apt III')
bio_data['full_names'] = bio_data['full_names'].str.replace('N. Davis','N. Jan Davis')
bio_data['full_names'] = bio_data['full_names'].str.replace('Michael Clifford','Michael R. Clifford')
bio_data['full_names'] = bio_data['full_names'].str.replace('Jerry Ross','Jerry L. Ross')
bio_data['full_names'] = bio_data['full_names'].str.replace('Bernard Harris','Bernard A. Harris Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Searfoss','Richard A. Searfoss')
bio_data['full_names'] = bio_data['full_names'].str.replace('William McArthur','William S. McArthur Jr.')

bio_data['full_names'] = bio_data['full_names'].str.replace('James Halsell','James D. Halsell Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Donald Thomas','Donald A. Thomas')
bio_data['full_names'] = bio_data['full_names'].str.replace('James Wetherbee','James D. Wetherbee')
bio_data['full_names'] = bio_data['full_names'].str.replace('Scott Horowitz','Scott J. Horowitz')
bio_data['full_names'] = bio_data['full_names'].str.replace('Terrence Wilcutt','Terrence W. Wilcutt')
bio_data['full_names'] = bio_data['full_names'].str.replace('James Reilly','James F. Reilly II')
bio_data['full_names'] = bio_data['full_names'].str.replace('James Newman','James H. Newman')
bio_data['full_names'] = bio_data['full_names'].str.replace('Edward Lu','Edward T. Lu')
bio_data['full_names'] = bio_data['full_names'].str.replace('Daniel Barry','Daniel T. Barry')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Mastracchio','Richard A. Mastracchio')
bio_data['full_names'] = bio_data['full_names'].str.replace('Jeffrey Ashby','Jeffrey S. Ashby')
bio_data['full_names'] = bio_data['full_names'].str.replace('John Phillips','John L. Phillips')
bio_data['full_names'] = bio_data['full_names'].str.replace('Yury Lonchakov','Yury V. Lonchakov')
bio_data['full_names'] = bio_data['full_names'].str.replace('Patrick Forrester','Patrick G. Forrester')
bio_data['full_names'] = bio_data['full_names'].str.replace('Pamela Melroy','Pamela A. Melroy')
bio_data['full_names'] = bio_data['full_names'].str.replace('Sandra Magnus','Sandra H. Magnus')
bio_data['full_names'] = bio_data['full_names'].str.replace('Lee Archambault','Lee J. Archambault')
bio_data['full_names'] = bio_data['full_names'].str.replace('Steven Swanson','Steven R. Swanson')
bio_data['full_names'] = bio_data['full_names'].str.replace('Clayton Anderson','Clayton C. Anderson')
bio_data['full_names'] = bio_data['full_names'].str.replace('Stephanie Wilson','Stephanie D. Wilson')

bio_data['full_names'] = bio_data['full_names'].str.replace('David Mackay','David W. D. Mackay')
bio_data['full_names'] = bio_data['full_names'].str.replace('Robert Behnken','Robert L. Behnken')
bio_data['full_names'] = bio_data['full_names'].str.replace('Thomas Marshburn','Thomas H. Marshburn')
bio_data['full_names'] = bio_data['full_names'].str.replace('Jean-Loup ChrÃ©tien','Jean-Loup Chrétien')
bio_data['full_names'] = bio_data['full_names'].str.replace('Michael LÃ³pez-AlegrÃ­a','Michael E. López-Alegría')



bio_data['full_names'] = bio_data['full_names'].str.replace('Russell Schweickart','Russell L. Schweickart')
bio_data['full_names'] = bio_data['full_names'].str.replace('Alfred Worden','Alfred M. Worden')
bio_data['full_names'] = bio_data['full_names'].str.replace('James Irwin','James B. Irwin')
bio_data['full_names'] = bio_data['full_names'].str.replace('Ronald Evans','Ronald E. Evans Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Harrison Schmitt','Harrison H. Schmitt')
bio_data['full_names'] = bio_data['full_names'].str.replace('Joseph Kerwin','Joseph P. Kerwin')
bio_data['full_names'] = bio_data['full_names'].str.replace('Paul Weitz','Paul J. Weitz')
bio_data['full_names'] = bio_data['full_names'].str.replace('Owen Garriott','Owen K. Garriott')
bio_data['full_names'] = bio_data['full_names'].str.replace('Gerald Carr','Gerald P. Carr')
bio_data['full_names'] = bio_data['full_names'].str.replace('Edward Gibson','Edward G. Gibson')
bio_data['full_names'] = bio_data['full_names'].str.replace('William Pogue','William R. Pogue')
bio_data['full_names'] = bio_data['full_names'].str.replace('Donald Slayton','Donald K. Slayton')
bio_data['full_names'] = bio_data['full_names'].str.replace('Thomas Mattingly','Thomas K. Mattingly II')
bio_data['full_names'] = bio_data['full_names'].str.replace('William Lenoir','William B. Lenoir')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Truly','Richard H. Truly')
bio_data['full_names'] = bio_data['full_names'].str.replace('Terry Hart','Terry J. Hart')
bio_data['full_names'] = bio_data['full_names'].str.replace('Anna Fisher','Anna L. Fisher')
bio_data['full_names'] = bio_data['full_names'].str.replace('Karol Bobko','Karol J. Bobko')
bio_data['full_names'] = bio_data['full_names'].str.replace('Donald Williams','Donald E. Williams')
bio_data['full_names'] = bio_data['full_names'].str.replace('S. Griggs','S. David Griggs')
bio_data['full_names'] = bio_data['full_names'].str.replace('Don Lind','Don Lind')
bio_data['full_names'] = bio_data['full_names'].str.replace('Taylor Wang','Taylor G. Wang')

bio_data['full_names'] = bio_data['full_names'].str.replace('Sultan Al Saud','Sultan bin Salman Al Saud')
bio_data['full_names'] = bio_data['full_names'].str.replace('Roy Bridges','Roy D. Bridges Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Karl Henize','Karl G. Henize')
bio_data['full_names'] = bio_data['full_names'].str.replace('Anthony England','Anthony W. England')
bio_data['full_names'] = bio_data['full_names'].str.replace('Loren Acton','Loren W. Acton')
bio_data['full_names'] = bio_data['full_names'].str.replace('John-David Bartoe','John-David F. Bartoe')
bio_data['full_names'] = bio_data['full_names'].str.replace('John Lounge','John M. Lounge')
bio_data['full_names'] = bio_data['full_names'].str.replace('William Fisher','William F. Fisher')
bio_data['full_names'] = bio_data['full_names'].str.replace('Charles Bolden','Charles F. Bolden Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Clarence Nelson','Clarence W. Nelson II')
bio_data['full_names'] = bio_data['full_names'].str.replace('Robert Cenker','Robert J. Cenker')
bio_data['full_names'] = bio_data['full_names'].str.replace('Michael Smith','Michael J. Smith')
bio_data['full_names'] = bio_data['full_names'].str.replace('Ellison Onizuka','Ellison S. Onizuka')
bio_data['full_names'] = bio_data['full_names'].str.replace('Ronald McNair','Ronald E. McNair')
bio_data['full_names'] = bio_data['full_names'].str.replace('Gregory Jarvis','Gregory B. Jarvis')
bio_data['full_names'] = bio_data['full_names'].str.replace('S. McAuliffe','S. Christa McAuliffe')
bio_data['full_names'] = bio_data['full_names'].str.replace('Alexander Aleksandrov','Alexander P. Aleksandrov')
bio_data['full_names'] = bio_data['full_names'].str.replace('Aleksandr Aleksandrov','Aleksandr P. Aleksandrov')
bio_data['full_names'] = bio_data['full_names'].str.replace('Abdul Mohmand','Abdul Ahad Mohmand')
bio_data['full_names'] = bio_data['full_names'].str.replace('James Bagian','James P. Bagian')
bio_data['full_names'] = bio_data['full_names'].str.replace('Manley Carter','Manley L. Carter Jr.')

bio_data['full_names'] = bio_data['full_names'].str.replace('Alan Shepard','Alan B. Shepard Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Aleksandr Balandin','Aleksandr N. Balandin')
bio_data['full_names'] = bio_data['full_names'].str.replace('John Casper','John H. Casper')
bio_data['full_names'] = bio_data['full_names'].str.replace('David Hilmers','David C. Hilmers')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Richards','Richard N. Richards')
bio_data['full_names'] = bio_data['full_names'].str.replace('William Shepherd','William M. Shepherd')
bio_data['full_names'] = bio_data['full_names'].str.replace('Carl Meade','Carl J. Meade')
bio_data['full_names'] = bio_data['full_names'].str.replace('Kenneth Reightler','Kenneth S. Reightler Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Mark Brown','Mark N. Brown')
bio_data['full_names'] = bio_data['full_names'].str.replace('Mario Runco','Mario Runco Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Thomas Hennen','Thomas J. Hennen')
bio_data['full_names'] = bio_data['full_names'].str.replace('Mae Jemison','Mae C. Jemison')
bio_data['full_names'] = bio_data['full_names'].str.replace('Charles Precourt','Charles J. Precourt')
bio_data['full_names'] = bio_data['full_names'].str.replace('Ronald Grabe','Ronald J. Grabe')
bio_data['full_names'] = bio_data['full_names'].str.replace('G. Low','G. David Low')
bio_data['full_names'] = bio_data['full_names'].str.replace('Peter Wisoff','Peter J. K. Wisoff')
bio_data['full_names'] = bio_data['full_names'].str.replace('Martin Fettman','Martin J. Fettman')
bio_data['full_names'] = bio_data['full_names'].str.replace('Sidney Gutierrez','Sidney M. Gutierrez')
bio_data['full_names'] = bio_data['full_names'].str.replace('Linda Godwin','Linda M. Godwin')
bio_data['full_names'] = bio_data['full_names'].str.replace('Thomas Jones','Thomas D. Jones')
bio_data['full_names'] = bio_data['full_names'].str.replace('Carl Walz','Carl E. Walz')
bio_data['full_names'] = bio_data['full_names'].str.replace('Yelena Kondakova','Yelena V. Kondakova')
bio_data['full_names'] = bio_data['full_names'].str.replace('Eileen Collins','Eileen M. Collins')

bio_data['full_names'] = bio_data['full_names'].str.replace('C. Foale','C. Michael Foale')
bio_data['full_names'] = bio_data['full_names'].str.replace('Catherine Coleman','Catherine G. Coleman')
bio_data['full_names'] = bio_data['full_names'].str.replace('Frederick Leslie','Frederick W. Leslie')
bio_data['full_names'] = bio_data['full_names'].str.replace('Albert Sacco','Albert Sacco Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Joseph Tanner','Joseph R. Tanner')
bio_data['full_names'] = bio_data['full_names'].str.replace('Gregory Harbaugh','Gregory J. Harbaugh')
bio_data['full_names'] = bio_data['full_names'].str.replace('Steven Smith','Steven L. Smith')
bio_data['full_names'] = bio_data['full_names'].str.replace('Susan Kilrain Still','Susan L. Kilrain Still')
bio_data['full_names'] = bio_data['full_names'].str.replace('Michael Gernhardt','Michael L. Gernhardt')
bio_data['full_names'] = bio_data['full_names'].str.replace('Roger Crouch','Roger K. Crouch')
bio_data['full_names'] = bio_data['full_names'].str.replace('Gregory Linteris','Gregory T. Linteris')
bio_data['full_names'] = bio_data['full_names'].str.replace('Robert Curbeam','Robert L. Curbeam Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Stephen Robinson','Stephen K. Robinson')
bio_data['full_names'] = bio_data['full_names'].str.replace('Michael Bloomfield','Michael J. Bloomfield')
bio_data['full_names'] = bio_data['full_names'].str.replace('Wendy Lawrence','Wendy B. Lawrence')
bio_data['full_names'] = bio_data['full_names'].str.replace('Joe Edwards','Joe F. Edwards Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Michael Anderson','Michael P. Anderson')
bio_data['full_names'] = bio_data['full_names'].str.replace('Andrew Thomas','Andrew S. W. Thomas')
bio_data['full_names'] = bio_data['full_names'].str.replace('Kathryn Hire','Kathryn P. Hire')
bio_data['full_names'] = bio_data['full_names'].str.replace('Jay Buckey','Jay C. Buckey')
bio_data['full_names'] = bio_data['full_names'].str.replace('James Pawelczyk','James A. Pawelczyk')

bio_data['full_names'] = bio_data['full_names'].str.replace('Rick Husband','Rick D. Husband')
bio_data['full_names'] = bio_data['full_names'].str.replace('Ellen Ochoa','Ellen L. Ochoa')
bio_data['full_names'] = bio_data['full_names'].str.replace('Tamara Jernigan','Tamara E. Jernigan')
bio_data['full_names'] = bio_data['full_names'].str.replace('Daniel Burbank','Daniel C. Burbank')
bio_data['full_names'] = bio_data['full_names'].str.replace('Dennis Tito','Dennis A. Tito')
bio_data['full_names'] = bio_data['full_names'].str.replace('Vladimir Dezhurov','Vladimir N. Dezhurov')
bio_data['full_names'] = bio_data['full_names'].str.replace('Duane Carey','Duane G. Carey')
bio_data['full_names'] = bio_data['full_names'].str.replace('John Grunsfeld','John M. Grunsfeld')
bio_data['full_names'] = bio_data['full_names'].str.replace('Michael Massimino','Michael J. Massimino')
bio_data['full_names'] = bio_data['full_names'].str.replace('Piers Sellers','Piers J. Sellers')
bio_data['full_names'] = bio_data['full_names'].str.replace('William Binnie','William B. Binnie')
bio_data['full_names'] = bio_data['full_names'].str.replace('Gregory Olsen','Gregory H. Olsen')
bio_data['full_names'] = bio_data['full_names'].str.replace('John Olivas','John D. Olivas')
bio_data['full_names'] = bio_data['full_names'].str.replace('George Zamka','George D. Zamka')
bio_data['full_names'] = bio_data['full_names'].str.replace('Douglas Wheelock','Douglas H. Wheelock')
bio_data['full_names'] = bio_data['full_names'].str.replace('Daniel Tani','Daniel M. Tani')
bio_data['full_names'] = bio_data['full_names'].str.replace('Dominic Gorie','Dominic L. P. Gorie')
bio_data['full_names'] = bio_data['full_names'].str.replace('Gregory Johnson','Gregory H. Johnson')
bio_data['full_names'] = bio_data['full_names'].str.replace('Michael Foreman','Michael J. Foreman')
bio_data['full_names'] = bio_data['full_names'].str.replace('Garrett Reisman','Garrett E. Reisman')
bio_data['full_names'] = bio_data['full_names'].str.replace('E. Fincke','E. Michael Fincke')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Garriott','Richard A. Garriott')


bio_data['full_names'] = bio_data['full_names'].str.replace('Dominic Antonelli','Dominic A. Antonelli')
bio_data['full_names'] = bio_data['full_names'].str.replace('Joseph Acaba','Joseph M. Acaba')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Arnold','Richard R. Arnold II')
bio_data['full_names'] = bio_data['full_names'].str.replace('Mark Polansky','Mark L. Polansky')
bio_data['full_names'] = bio_data['full_names'].str.replace('Christopher Cassidy','Christopher J. Cassidy')
bio_data['full_names'] = bio_data['full_names'].str.replace('Timothy Kopra','Timothy L. Kopra')
bio_data['full_names'] = bio_data['full_names'].str.replace('Timothy Creamer','Timothy J. Creamer')
bio_data['full_names'] = bio_data['full_names'].str.replace('Alan Poindexter','Alan G. Poindexter')
bio_data['full_names'] = bio_data['full_names'].str.replace('James Dutton','James P. Dutton Jr.')
bio_data['full_names'] = bio_data['full_names'].str.replace('Dorothy Metcalf-Lindenburger','Dorothy M. Metcalf-Lindenburger')
bio_data['full_names'] = bio_data['full_names'].str.replace('Christopher Ferguson','Christopher J. Ferguson')
bio_data['full_names'] = bio_data['full_names'].str.replace('Rex Walheim','Rex J. Walheim')
bio_data['full_names'] = bio_data['full_names'].str.replace('Sunita Williams','Sunita L. Williams')
bio_data['full_names'] = bio_data['full_names'].str.replace('Karen Nyberg','Karen L. Nyberg')
bio_data['full_names'] = bio_data['full_names'].str.replace('Richard Branson','Sir Richard Branson')
bio_data['full_names'] = bio_data['full_names'].str.replace('Robert White','Robert M. White')
bio_data['full_names'] = bio_data['full_names'].str.replace('George Nield','Dr. George Nield')
bio_data['full_names'] = bio_data['full_names'].str.replace('Anton Shkaplerov','Anton N. Shkaplerov')
bio_data['full_names'] = bio_data['full_names'].str.replace('William Dana','William H. Dana')


bio_data['full_names'] = bio_data['full_names'].str.replace('Sigmund JÃ¤hn','Sigmund Jähn')
bio_data['full_names'] = bio_data['full_names'].str.replace('Jean-Pierre HaignerÃ©','Jean-Pierre Haigneré')
bio_data['full_names'] = bio_data['full_names'].str.replace('Claudie HaignerÃ©','Claudie Haigneré')

bio_data['full_names'] = bio_data['full_names'].str.replace('Franz ViehbÃ¶ck','Franz A. Viehböck')
bio_data['full_names'] = bio_data['full_names'].str.replace('Franklin Chang DÃ­a','Franklin R. Chang Díaz')
bio_data['full_names'] = bio_data['full_names'].str.replace('Pháº¡m TuÃ¢n','Phạm Tuân')
bio_data['full_names'] = bio_data['full_names'].str.replace('Soichi Noguch','Sôichi Noguchi')
bio_data['full_names'] = bio_data['full_names'].str.replace('JÃ¼gderdemidiin GÃ¼rragchaa','Jügderdemidiin Gürragchaa')

