# uupeeps

This package is an interface to the public staff information on https://www.uu.nl/staff/. This package was created by Class CoTaPP in a live coding session led by Jonathan de Bruin. The aim was to create and publish a Python package in 30 minutes. 

## Installation

Instal the package with 

```
pip install git+https://github.com/UtrechtUniversity/uupeeps
```

## Usage

Import the package:

```
import uupeeps
```
Get employees per faculty:

```
uupeeps.get_employees_url(5)
```

Get employee info (e.g. https://www.uu.nl/staff/ALLamprecht/):

```
>>> uupeeps.get_employee_info("ALLamprecht")

{
   "Guid":"30936d707a9546e6b768c707473c4366",
   "Activities":[
      
   ],
   "ActivitiesFreeText":"None",
   "AdditionalFunctions":"None",
   "Availability":"None",
   "Bio":"None",
   "CV":"<p>Short biography:</p>\n<ul>\n<li>Since 2017: Assistant Professor of Software Technology (here)</li>\n<li>2015 - 2017: Research Fellow at Lero - The Irish Software Research Centre at the University of Limerick, Ireland</li>\n<li>2012 - 2015: Postdoctoral Researcher at the Chair of Service and Software Engineering, Institute of Computer Sciene, University of Potsdam, Germany</li>\n<li>2007 - 2012: PhD Student and Research Assistant at the Chair of Programming Systems, Faculty of Computer Science, TU Dortmund University, Germany. My thesis <a href=\"https://doi.org/10.1007/978-3-642-45389-2\">\"User-Level Workflow Design. A Bioinformatics Perspective.\"</a> was graded \"with distinction\", honored with the faculty\\'s dissertation award and published in Springer\\'s LNCS series.</li>\n<li>2002 - 2007: B.Sc./M.Sc. student of Applied Computer Science at the University of G&ouml;ttingen, Germany</li>\n</ul>\n<p>If you are interested in more elaborate version of my CV, please contact me by e-mail and I will be happy to send you an up-to-date document.&nbsp;</p>",
   "CVUrl":"None",
   "Chair":"None",
   "ContactDetails":[
      {
         "Guid":"06c7175e58b34c3ea59cea51f43bb1d8",
         "Address":"Princetonplein 5",
         "Building":"Buys Ballotgebouw",
         "City":"Utrecht",
         "Id":398232,
         "Phone":"030 253 3261",
         "PhoneDepartment":"None",
         "Room":"5.65",
         "Url":"None",
         "Zipcode":"3584 CC"
      }
   ],
   "ContactFreeText":"None",
   "Courses":[
      {
         "Guid":"168305df221e4eb3bb501f92d2271e98",
         "Code":"INFOMCTH",
         "ECTS":"None",
         "Id":232243,
         "Level":"None",
         "Name":"Computational thinking",
         "Type":"None",
         "Url":"https://osiris.uu.nl/osiris_student_uuprd/OnderwijsCatalogusSelect.do?selectie=cursus&cursus=INFOMCTH&collegejaar=2020&taal=nl"
      },
      {
         "Guid":"6035a5b64a3d4f8290b71baa559a8ebf",
         "Code":"INFOMPSV",
         "ECTS":"None",
         "Id":232244,
         "Level":"None",
         "Name":"Programmasemantiek en -verificatie",
         "Type":"None",
         "Url":"https://osiris.uu.nl/osiris_student_uuprd/OnderwijsCatalogusSelect.do?selectie=cursus&cursus=INFOMPSV&collegejaar=2020&taal=nl"
      },
      {
         "Guid":"3e3e174cac624cb1a3c806421a3cefdc",
         "Code":"BETA-B1PYT",
         "ECTS":"None",
         "Id":232245,
         "Level":"None",
         "Name":"Programmeren met Python",
         "Type":"None",
         "Url":"https://osiris.uu.nl/osiris_student_uuprd/OnderwijsCatalogusSelect.do?selectie=cursus&cursus=BETA-B1PYT&collegejaar=2020&taal=nl"
      },
      {
         "Guid":"195b18705fb949a7a328c4cf0646bcec",
         "Code":"INFOB2PWD",
         "ECTS":"None",
         "Id":232241,
         "Level":"None",
         "Name":"Programming with data",
         "Type":"None",
         "Url":"https://osiris.uu.nl/osiris_student_uuprd/OnderwijsCatalogusSelect.do?selectie=cursus&cursus=INFOB2PWD&collegejaar=2020&taal=nl"
      },
      {
         "Guid":"3f9d95542948442fa28a36eca2215eca",
         "Code":"INFOSP",
         "ECTS":"None",
         "Id":232242,
         "Level":"None",
         "Name":"Softwareproject",
         "Type":"None",
         "Url":"https://osiris.uu.nl/osiris_student_uuprd/OnderwijsCatalogusSelect.do?selectie=cursus&cursus=INFOSP&collegejaar=2020&taal=nl"
      }
   ],
   "CoursesFreeText":"<p>Teaching is an essential part of academic life that I enjoy very much. I have more than 15 years of experience teaching courses on various topics at different places, in several study programs and with many formats and group sizes. I possess a University Teaching Qualification (BKO) from Utrecht University and a Senior Teaching Professionals certificate from the Potsdam University Graduate School. In Utrecht I teach different courses related to programming, software engineering and formal methods to both ICS and non-ICS students. English is my main medium of instruction, but students are also welcome to approach me in Dutch or German.</p>\n<p><strong>Projects<br /></strong>Feel free to contact me if you are interested in doing a Master thesis, Bachelor thesis or any other kind of project in the context of <a href=\"https://www.uu.nl/staff/allamprecht/Research\">my research topics</a>. There are always interesting things to do! Some concrete ideas for thesis projects are available at <a href=\"https://uu.konjoin.nl/profile/anna-lena-lamprecht\">my KonJoin page</a>, but there are always more and I am happy to discuss any other ideas.&nbsp;</p>",
   "CustomTab1":"None",
   "CustomTab2":"None",
   "CustomTab3":"None",
   "DateInauguralLecture":"None",
   "DateOfAppointment":"None",
   "Email":"a.l.lamprecht@uu.nl",
   "EndowedBy":"None",
   "Expertises":[
      {
         "Guid":"a63e139b270a413885f3cd11a7dc63ce",
         "Id":17583,
         "Name":"Onderzoekssoftware",
         "Url":"/medewerkers/organogram?expertise=10355"
      },
      {
         "Guid":"9a70e1e62d7441669722cd45ba964ebf",
         "Id":17582,
         "Name":"Softwareontwikkeling",
         "Url":"/medewerkers/organogram?expertise=2493"
      },
      {
         "Guid":"c4608d5a62df4f0aa714ef8fafdfd0c4",
         "Id":18652,
         "Name":"Formele methoden",
         "Url":"/medewerkers/organogram?expertise=10392"
      },
      {
         "Guid":"dfffa59b8abb48a3b18f2fa676bb0b52",
         "Id":18653,
         "Name":"Open Science",
         "Url":"/medewerkers/organogram?expertise=10286"
      }
   ],
   "Faculties":[
      {
         "Guid":"2c451e20740b444ea7e298f8eab586f4",
         "ChildCount":"None",
         "Code":"None",
         "Faculty":"B??tawetenschappen",
         "FacultyId":5,
         "FacultyUrl":"https://www.uu.nl/organisatie/faculteit-betawetenschappen",
         "MainPosition":true
      }
   ],
   "FocusAreas":[
      {
         "Guid":"2d3ca2c6ea5045bfbde732a22bada7c4",
         "Id":11897,
         "Name":"Applied Data Science",
         "Url":"/medewerkers/organogram?focusarea=29"
      },
      {
         "Guid":"1552833042ae4797ae5b27dacb5c1a55",
         "Id":13675,
         "Name":"Human-centered Artificial Intelligence",
         "Url":"/medewerkers/organogram?focusarea=32"
      },
      {
         "Guid":"c3307ce0d07a4883bd6c66f0e5305329",
         "Id":5657,
         "Name":"Integrative Bioinformatics",
         "Url":"/medewerkers/organogram?focusarea=13"
      },
      {
         "Guid":"9a3d6d779fc64c3684cc942785fd83aa",
         "Id":13676,
         "Name":"Life Sciences",
         "Url":"/medewerkers/organogram?focusarea=19"
      },
      {
         "Guid":"40f92b8726e54775ad579f2b4974c212",
         "Id":5484,
         "Name":"Utrecht Platform for Applied Data Science",
         "Url":"/medewerkers/organogram?focusarea=27"
      }
   ],
   "Id":33086,
   "Images":[
      
   ],
   "KeyPublications":{
      "Guid":"7cba9f92ee1f487b9ac890a554b4d1de",
      "GroupType":"None",
      "Groupname":"Sleutelpublicaties",
      "Publications":[
         
      ]
   },
   "LastUpdate":"/Date(1613590448380+0100)/",
   "Links":[
      
   ],
   "LinksSocialMedia":[
      {
         "Guid":"929d43d61ca849a09253842f84a58e78",
         "IconUrl":"https://www.uu.nl/medewerkers/static/SocialMedia/linkedin.com.png",
         "Id":12783,
         "Name":"LinkedIn",
         "Url":"https://www.linkedin.com/in/alamprecht/"
      },
      {
         "Guid":"99a9884609994ca7a5147b785452060d",
         "IconUrl":"https://www.uu.nl/medewerkers/static/SocialMedia/orcid.org.png",
         "Id":12828,
         "Name":"ORCID",
         "Url":"https://orcid.org/0000-0003-1953-5606"
      },
      {
         "Guid":"8ed25440a9ea4befbe1b7a36be8ecf73",
         "IconUrl":"https://www.uu.nl/medewerkers/static/SocialMedia/twitter.com.png",
         "Id":14851,
         "Name":"Twitter",
         "Url":"https://twitter.com/al_lamprecht"
      }
   ],
   "Media":"None",
   "MediaFreeText":"None",
   "MobileNumber":"None",
   "Name":"Dr. A.L. (Anna-Lena) Lamprecht",
   "NameShort":"A.L. (Anna-Lena) Lamprecht",
   "OnlyEN":false,
   "Organisation":"Universiteit Utrecht",
   "PhotoUrl":"/Public/GetImage?Employee=33086&_t=08042021213657&t=",
   "Positions":[
      {
         "Guid":"9469fae59d514b6689476fdb1ead5bdb",
         "Level1":"B??tawetenschappen",
         "Level1Url":"https://www.uu.nl/medewerkers/organogram/beta",
         "Level2":"Informatica",
         "Level2Url":"https://www.uu.nl/medewerkers/organogram/beta/87",
         "Level3":"Intelligent Software Systems",
         "Level3Url":"https://www.uu.nl/medewerkers/organogram/beta/87/849",
         "Level4":"Software Technology",
         "Level4Url":"https://www.uu.nl/medewerkers/organogram/beta/87/849/858",
         "Order":0,
         "Position":"Universitair docent",
         "PositionId":93
      }
   ],
   "PostalAddress":"None",
   "Prizes":[
      
   ],
   "PrizesFreeText":"None",
   "Profile":"<p>Hi, I am Anna-Lena Lamprecht. I work as an assistant professor in the <a href=\"https://www.uu.nl/en/research/software-systems/software-technology\">Software Technology group</a> at the Department of Information and Computing Sciences. I conduct research at the interface of (research) software engineering and applied formal methods, currently focusing on FAIR software and automated composition of scientific workflows. I teach courses on programming, software engineering and formal methods in the department\\'s study programs and beyond. I am a <a href=\"https://www.uu.nl/en/organisation/faculty-of-science/about-us/westerdijk-fellowship\">Westerdijk Fellow</a>, Faculty Ambassador of the <a href=\"https://openscience-utrecht.com/\">Open Science Community Utrecht</a>, and co-founder and steering committee member of the <a href=\"https://www.uu.nl/en/news/diversity-inclusion-award-for-young-women-in-geoscience-and-for-women-in-information-and-computing\">award-winning</a> Women in Information and Computing Sciences (<a href=\"https://wics.sites.uu.nl/\">WICS</a>) network. I am active in several national and international communities, including <a href=\"https://de-rse.org/\">de-RSE</a>, <a href=\"http://easst.aulp.co.uk/\">EASST</a>, <a href=\"https://elixir-europe.org/\">ELIXIR</a>, <a href=\"http://www.fmeurope.org/\">FME</a>, <a href=\"https://ict-research.nl/\">IPN</a>, <a href=\"https://nl-rse.org/\">NL-RSE</a> and <a href=\"https://www.versen.nl/\">VERSEN</a>. I am an NL-RSE core team member, Netherlands representative at the International Council of RSE Associations, secretary of the IPN EDI working group, and co-editor-in-chief of the open-access journal <a href=\"https://journal.ub.tu-berlin.de/eceasst\">ECEASST</a>.</p>\n<p>More about me:</p>\n<ul>\n<li>Article about me and my work for the <a href=\"https://ict-research.nl/wordpress/wp-content/uploads/2019/01/IO-magazine-NR04-december-2018_v4-_web.pdf\">I/O Magazine December 2018</a> (last page), by <a href=\"https://amandaschrijft.nl/\">Amanda Verdonk</a>.</li>\n<li><a href=\"https://ubc.uu.nl/anna-lenas-expertise-software-technology/\">Interview</a> for the May 2020 newsletter of the <a href=\"https://ubc.uu.nl/\">Utrecht Bioinformatics Center</a>, by <a href=\"https://www.uu.nl/medewerkers/CJNijenhuis\">Celia Nijenhuis</a>.&nbsp;</li>\n<li><a href=\"https://openscience-utrecht.com/2020/09/19/introducing-the-oscu-faculty-ambassadors-v-anna-lena-lamprecht-faculty-of-science/\">Interview</a> for the <a href=\"https://openscience-utrecht.com/r2os/\">Road to Open Science blog</a> in September 2020, by <a href=\"https://stefangaillard.com/\">Stefan Gaillard</a>.</li>\n</ul>\n<p>&nbsp;</p>",
   "Projects":[
      
   ],
   "ProjectsCompleted":[
      
   ],
   "ProjectsFreeTextBottom":"None",
   "ProjectsFreeTextTop":"<p>I conduct research at the interface of <strong><a href=\"https://en.wikipedia.org/wiki/Research_software_engineering\">(research) software engineering</a></strong> and <strong>applied <a href=\"https://en.wikipedia.org/wiki/Formal_methods\">formal methods</a></strong>. Research software engineering (RSE) is an emerging discipline that studies research software and its development processes, and develops methods, techniques and tools to improve them. As research in most scholarly disciplines today critically depends on software, RSE is rapidly gaining importance. In particular, research-specific quality assurance methods for software are urgently needed to ensure correct, reliable and reproducible research results. My goal is to leverage the potential of formal methods to help researchers develop higher-quality software with less effort.&nbsp;</p>\n<p>My current research focus is on the use of process synthesis techniques for the exploration of computational pipelines (a.k.a. scientific workflows). <a href=\"https://www.uu.nl/staff/VKasalica\">Vedran Kasalica</a> has joined me in Utrecht as a PhD candidate in this area. We have developed <strong>the</strong> <strong><a href=\"https://github.com/sanctuuary/APE\">Automated Pipeline Explorer (APE)</a></strong> a command line tool and Java API for the automated exploration of possible computational pipelines from large collections of computational tools. We use APE in different collaborative projects in bioinformatics and the geosciences, most notably:&nbsp;</p>\n<ul>\n<li>\n<p><strong>Automated workflow discovery and composition in mass spectrometry-based proteomics. </strong>This is a collaboration with <a href=\"https://orcid.org/0000-0001-6666-1520\">Jon Ison</a> (AstraZeneca), <a href=\"https://orcid.org/0000-0002-5865-8994\">Magnus Palmblad</a> (University of Leiden Medical Center), <a href=\"https://orcid.org/0000-0002-9708-6722\">Veit Schw&auml;mmle</a> (University of Southern Denmark) and other collaborators from the <a href=\"https://elixir-europe.org/\">ELIXIR</a> network. We use APE for the composition of bioinformatics tools for the analysis of mass spectrometry data into purpose-specific workflows. The tools (from ms-utils.org and <a href=\"https://bio.tools/\">bio.tools</a>) are semantically annotated with terms from the <a href=\"http://edamontology.org/page\">EDAM</a> ontology.</p>\n</li>\n<li>\n<p><strong>Automated workflow discovery and composition in QuAnGIS.&nbsp;</strong><a href=\"https://questionbasedanalysis.com/\">QuAnGIS</a> (Question-based Analysis of Geographic Information with Semantic Queries) is an ERC Starting Grant project led by <a href=\"https://orcid.org/0000-0002-2267-4810\">Simon Scheider</a> (Faculty of Geosciences), which aims at developing a novel theory of interrogative spatial concepts to turn geoanalytical questions into a machine-readable form using semantic queries. In this form, questions can directly be matched with the capacity of major analytic GIS tools and data on the Web. Often the answer to the queries does however not yet exists and needs to be computed first, meaning that a suitable workflow has to be constructed to answer the query. We started to work together to solve this problem with workflow synthesis technology.</p>\n</li>\n</ul>\n<p>Furthermore, I am actively involved in the international collaborative work on <strong><a href=\"https://www.rd-alliance.org/groups/fair-research-software-fair4rs-wg\">FAIR Principles for Research Software</a></strong> and lead author of <a href=\"https://doi.org/10.3233/DS-190026\">one of the first major papers on the topic</a>, and in the discussion around research challenges within RSE.&nbsp;</p>",
   "Publications":[
      {
         "Guid":"5bd97e63e7c2445bacd66844b9486632",
         "GroupType":"None",
         "Groupname":"2020 - Artikelen",
         "Publications":[
            "Kruiger, J.F., Kasalica, V., Meerlo, Rogier, Lamprecht, A.L., Nyamsuren, E. &amp; Scheider, S. (26-10-2020). <i><a href=\"https://doi.org/10.1111/TGIS.12692\" target=\"_blank\">Loose programming of GIS workflows with geo-analytical concepts</a></i>.  <i>Transactions in GIS</i> ",
            "Scheider, S., Meerlo, Rogier, Kasalica, V. &amp; Lamprecht, A.L. (2020). <i><a href=\"https://doi.org/10.5311/JOSIS.2020.20.555\" target=\"_blank\">Ontology of core concept data types for answering geo-analytical questions</a></i>.  <i>Journal of Spatial Information Science</i>, 2020 (20) (35 p.). ",
            "Kasalica, V. &amp; Lamprecht, A.L. (2020). <i><a href=\"http://dspace.library.uu.nl/handle/1874/396824\" target=\"_blank\">Workflow Discovery with Semantic Constraints: The SAT-Based Implementation of APE</a></i>.  <i>Electronic Communications of the EASST</i>, 78 (25 p.). "
         ]
      },
      {
         "Guid":"78f42eae494c42c4abd85ebfa0433787",
         "GroupType":"None",
         "Groupname":"2020 - Artikelen in bundels / proceedings",
         "Publications":[
            "Kasalica, V. &amp; Lamprecht, A.L. (2020). <i><a href=\"https://doi.org/10.1007/978-3-030-50436-6_34\" target=\"_blank\">APE: A Command-Line Tool and API for Automated Workflow Composition</a></i>.  <i>Proceedings of the International Conference on Computational Science (ICCS 2020)</i> (12 p.). Springer.",
            "Akhuseyinoglu, Kamil, Barria-Pineda, Jordan, Sosnovsky, Sergey, Lamprecht, Anna-Lena, Guerra, Julio &amp; Brusilovsky, Peter (2020). <i><a href=\"https://doi.org/10.1007/978-3-030-57717-9_18\" target=\"_blank\">Exploring Student-Controlled Social Comparison</a></i>. In Carlos Alario-Hoyos, Mar&#237;a Jes&#250;s Rodr&#237;guez-Triana, Maren Scheffel, Inmaculada Arnedillo-S&#225;nchez &amp; Sebastian Maximilian Dennerlein (Eds.),  <i>Addressing Global Challenges and Quality Education - 15th European Conference on Technology Enhanced Learning, EC-TEL 2020, Heidelberg, Germany, September 14???18, 2020, Proceedings</i> (pp. 244-258) (15 p.). Cham: Springer, Cham."
         ]
      },
      {
         "Guid":"8c0e63de30b54b21a80f2c612c6653a5",
         "GroupType":"None",
         "Groupname":"2020 - Overige resultaten",
         "Publications":[
            "Sufi, Shoaib, Ortiz, Carlos Martinez, Hof, Cees, Aerts, Patrick, Klinkenberg, Adriaan, Lamprecht, Anna-Lena, Sierman, Barbara, Willigen, Bettine van, Olivier, Brett, Willing, Carol, Thiel, Carsten, Leeuwen, Caspar van, Jones, Catherine, Flach, Christina von, Katz, Daniel S., Hansen, Dominique, Plomp, Esther, Coen, Gerard, Steptoe, Hamish, Bosma, Hannah, Andrews, Heather, Davenport, James, Shiers, Jamie, Vos, Jesse de, Knijff, Johan van der, Spaaks, Jurriaan H., Kavoussanakis, Kostas, Garcia, Leyla, Behn, Mario, David, Mario, Kuzak, Mateusz, Hong, Neil Chue, Dintzner, Nicolas, Orviz, Pablo, Lavanchy, Paula Martinez, Doorn, Peter, Kotarski, Rachael, Silva, Raniere, Haines, Robert, Cosmo, Roberto di, Overgoor, Skip, Druskat, Stephan, Sandt, Stephanie van de, Boom, Tim van den, Letizia, Viviana, Seuskens, Wiel &amp; Moranville, Yoann (01-07-2020). <i><a href=\"https://doi.org/10.5281/zenodo.3922155\" target=\"_blank\">Report on the Workshop on Sustainable Software Sustainability 2019 (WOSSS19)</a></i>.  <i></i> "
         ]
      },
      {
         "Guid":"c40b384427664809b0389557daf87456",
         "GroupType":"None",
         "Groupname":"2019 - Artikelen",
         "Publications":[
            "Palmblad, Magnus, Lamprecht, A.L., Ison, Jon &amp; Schw&#228;mmle, Veit (2019). <i><a href=\"http://dspace.library.uu.nl/handle/1874/379482\" target=\"_blank\">Automated workflow composition in mass spectrometry based proteomics</a></i>.  <i>Bioinformatics</i>, 35 (4), (pp. 656-664). ",
            "Ison, Jon, M&#233;nager, Herv&#233;, Brancotte, Bryan, Jaaniso, Erik, Salumets, Ahto, Ra??ek, Tom&#225;??, Lamprecht, Anna-Lena, Palmblad, Magnus, Kala??, Mat&#250;??, Chmura, Piotr, Hancock, John M, Schw&#228;mmle, Veit &amp; Ienasescu, Hans-Ioan (2019). <i><a href=\"http://dspace.library.uu.nl/handle/1874/385733\" target=\"_blank\">Community curation of bioinformatics software and data resources</a></i>.  <i>Briefings in Bioinformatics</i> (9 p.). ",
            "Lamprecht, Anna-Lena, Garcia, Leyla, Kuzak, Mateusz, Martinez, Carlos, Arcila, Ricardo, Martin Del Pico, Eva, Dominguez Del Angel, Victoria, van de Sandt, Stephanie, Ison, Jon, Martinez, Paula Andrea, McQuilton, Peter, Valencia, Alfonso, Harrow, Jennifer, Psomopoulos, Fotis, Gelpi, Josep Ll, Chue Hong, Neil, Goble, Carole &amp; Capella-Gutierrez, Salvador (13-11-2019). <i><a href=\"https://doi.org/10.3233/DS-190026\" target=\"_blank\">Towards FAIR principles for research software</a></i>.  <i>EPJ Data Science</i>, Preprint (Preprint), (pp. 1-23) (23 p.). "
         ]
      },
      {
         "Guid":"f857dc7a4e7f4526be0e184ce1928f69",
         "GroupType":"None",
         "Groupname":"2019 - Boekdelen / hoofdstukken",
         "Publications":[
            "Margaria, Tiziana &amp; Lamprecht, Anna-Lena (2019). <i><a href=\"https://doi.org/10.1007/978-3-319-60013-0_209-1\" target=\"_blank\">Modeling of Games and Game Strategies</a></i>. In Arthur Tatnall (Eds.),  <i>Encyclopedia of education and information technologies</i> (12 p.). Cham: Springer International Publishing.",
            "Lamprecht, Anna-Lena &amp; Margaria, Tiziana (2019). <i><a href=\"https://doi.org/10.1007/978-3-319-60013-0_210-1\" target=\"_blank\">Modeling of Scientific Workflows</a></i>. In Arthur Tatnall (Eds.),  <i>Encyclopedia of education and information technologies</i> (pp. 1-8) (8 p.). Cham: Springer."
         ]
      },
      {
         "Guid":"e7cb811ceb4343d2b843b7614a9c4c48",
         "GroupType":"None",
         "Groupname":"2019 - Artikelen in bundels / proceedings",
         "Publications":[
            "Kasalica, Vedran &amp; Lamprecht, Anna-Lena (2019). <i><a href=\"https://doi.org/10.1007/978-3-030-24302-9_34\" target=\"_blank\">Workflow Discovery Through Semantic Constraints -  A Geovisualization Case Study</a></i>. In Sanjay Misra, Osvaldo Gervasi, Beniamino Murgante, Elena Stankova, Vladimir Korkhov, Carmelo Torre, Ana Maria A.C. Rocha, David Taniar, Bernady O. Apduhan &amp; Eufemia Tarantino (Eds.),  <i>Computational Science and Its Applications -- ICCSA 2019 - 19th International Conference, Saint Petersburg, Russia, July 1-4, 2019, Proceedings</i> (pp. 473-488) (16 p.). Cham: Springer."
         ]
      },
      {
         "Guid":"7b156da4e7ed48a881c59d3e340dcaa3",
         "GroupType":"None",
         "Groupname":"2019 - Overige resultaten",
         "Publications":[
            "Erdmann, Christopher, Simons, Natasha, Otsuji, Reid, Labou, Stephanie, Johnson, Ryan, Castelao, Guilherme, Boas, Bia Villas, Lamprecht, Anna-Lena, Ortiz, Carlos Martinez, Garcia, Leyla, Kuzak, Mateusz, Martinez, Paula Andrea, Stokes, Liz, Honeyman, Tom, Wise, Sharyn, Quan, Josh, Peterson, Scott, Neeser, Amy, Karvovskaya, Lena, Lange, Otto, Witkowska, Iza, Flores, Jacques, Bradley, Fiona, Hettne, Kristina, Verhaar, Peter, Companjen, Ben, Sesink, Laurents, Schoots, Fieke, Schultes, Erik, Kaliyaperumal, Rajaram, T&#243;th-Czifra, Erzs&#233;bet, Azevedo, Ricardo de Miranda, Muurling, Sanne, Brown, John, Chan, Janice, Quigley, Niamh, Federer, Lisa, Joubert, Douglas, Dillman, Allissa, Wilkins, Kenneth, Chandramouliswaran, Ishwar, Navale, Vivek, Wright, Susan, Giorgio, Silvia Di, Fasemore, Mandela, F&#246;rstner, Konrad, Sauerwein, Till, Seidlmayer, Eva, Zeitlin, Ilja, Bacon, Susannah, Hannan, Katie, Ferrers, Richard, Russell, Keith, Whitmore, Deidre &amp; Dennis, Tim (01-02-2019). <i><a href=\"http://dspace.library.uu.nl/handle/1874/390076\" target=\"_blank\">Top 10 FAIR Data  Software Things</a></i>.  <i></i> "
         ]
      },
      {
         "Guid":"581ad517c294414ba8121c627e54af26",
         "GroupType":"None",
         "Groupname":"2019 - Abstract",
         "Publications":[
            "Lamprecht, A.L. (2019). <i><a href=\"https://www.iccs-meeting.org/iccs2019/wp-content/schedule/pages/WTCS1.html#abstract253\" target=\"_blank\">Computational Thinking and Programming with Python for Aspiring Data Scientists</a></i>.  <i></i> "
         ]
      },
      {
         "Guid":"a342324bbb25444f83a708340523dbe6",
         "GroupType":"None",
         "Groupname":"2019 - Prize (including medals and awards)",
         "Publications":[
            "Kasalica, V. &amp; Lamprecht, Anna-Lena 2019 Recipient ICCSA 2019 Best Paper Award "
         ]
      },
      {
         "Guid":"dad38315b24f4b4b9ae59ac6baa5d4e3",
         "GroupType":"None",
         "Groupname":"2018 - Boekdelen / hoofdstukken",
         "Publications":[
            "Margaria, Tiziana, Lamprecht, A.L. &amp; Steffen, Bernhard (2018). <i>Continuous Model-Driven Engineering</i>. In Mike Hinchey (Eds.),  <i>Software Technology - 10 Years of Innovation in IEEE Computer</i> Wiley."
         ]
      },
      {
         "Guid":"8c8162c2e04946db8cc24eaf31b735f8",
         "GroupType":"None",
         "Groupname":"2018 - Artikelen in bundels / proceedings",
         "Publications":[
            "Gossen, Frederik, K&#252;hn, Dennis, Margaria, Tiziana &amp; Lamprecht, A.L. (2018). <i><a href=\"https://doi.org/10.1109/COMPSAC.2018.00175\" target=\"_blank\">Computational Thinking: Learning by Doing with the Cinco Adventure Game Tool</a></i>.  <i>Proceedings of the 42nd IEEE International Conference on Computers, Software and Applications</i> ",
            "McInerney, Clare, Lamprecht, A.L. &amp; Margaria, Tiziana (2018). <i><a href=\"https://doi.org/10.1007/978-3-319-74310-3_50\" target=\"_blank\">Computing Camps for Girls - A First-Time Experience at the University of Limerick</a></i>. In Arthur Tatnall &amp; Mary Webb (Eds.),  <i>Tomorrow???s Learning: Involving Everyone - Learning with and about technologies and computing</i> (pp. 494-505). Heidelberg: Springer.",
            "Wickert, Alexander, Lamprecht, A.L. &amp; Margaria, Tiziana (2018). <i><a href=\"https://doi.org/10.1145/3193992.3194002\" target=\"_blank\">Domain-specific Design of Patient Classification in Cancer-Related Cachexia Research</a></i>.  <i>Proceedings of the 6th Conference on Formal Methods in Software Engineering, FormaliSE 2018, collocated with ICSE 2018, Gothenburg, Sweden, June 2, 2018.</i> (pp. 60-63). ACM."
         ]
      },
      {
         "Guid":"6f9444e283ea41dba57319c6f61a11e4",
         "GroupType":"None",
         "Groupname":"2018 - Editorial",
         "Publications":[
            "Maglyas, Andrey &amp; Lamprecht, A.L. (2018). <i><a href=\"https://doi.org/10.1016/j.jss.2017.10.003\" target=\"_blank\">Introduction to the special issue on ???Software Business???</a></i>.  <i>Journal of Systems and Software</i>, 135, (pp. 105-106) (2 p.). "
         ]
      },
      {
         "Guid":"0ab9f98cbefa44378d4ddf0b48922622",
         "GroupType":"None",
         "Groupname":"2018 - Poster",
         "Publications":[
            "Lamprecht, A.L., Palmblad, Magnus, Ison, Jon &amp; Schw&#228;mmle, Veit (2018). <i><a href=\"https://doi.org/10.1109/eScience.2018.00098\" target=\"_blank\">Automated Composition of Scientific Workflows in Mass Spectrometry-Based Proteomics</a></i>.  <i></i> ",
            "Kasalica, V. &amp; Lamprecht, A.L. (2018). <i><a href=\"https://doi.org/10.1109/eScience.2018.00099\" target=\"_blank\">Automated Composition of Scientific Workflows: A Case Study on Geographic Data Manipulation</a></i>.  <i></i> "
         ]
      },
      {
         "Guid":"f5272cfb7b054c2a880569f5c0e78425",
         "GroupType":"None",
         "Groupname":"2017 - Abstract",
         "Publications":[
            "Lamprecht, A.L. (2017). <i>Bridging Gaps with Scientific Workflows: Experiences from an Interdisciplinary Project Course</i>.  <i></i> ",
            "McInerney, Clare, Lamprecht, A.L. &amp; Margaria, Tiziana (2017). <i>Computing Camps for Girls - A First-Time Experience at the University of Limerick</i>.  <i></i> "
         ]
      },
      {
         "Guid":"6ae1db4306dc400ba098bc6cd0dfbaf0",
         "GroupType":"None",
         "Groupname":"2017 - Editorial activity",
         "Publications":[
            "Lamprecht, A.L. (2017) Guest editor Electronic Communications of the EASST (Journal) <em>Guest Editor for post-conference proceedings of the 7th International Symposium on Leveraging Applications of Formal Methods, Verification and Validation - Doctoral Symposium, 2016 (ISoLA DS 2016)</em>"
         ]
      },
      {
         "Guid":"2dcb6a2ebaa84138807787bea8576d90",
         "GroupType":"None",
         "Groupname":"2016 - Editorial activity",
         "Publications":[
            "Lamprecht, A.L. (2016) Editorial board member Electronic Communications of the EASST (Journal) <em>Co-Editor in Chief</em>",
            "Lamprecht, A.L. (2016) Guest editor Journal of Systems and Software (Journal) <em>Special Issue on &quot;Software Business&quot;</em>"
         ]
      }
   ],
   "PublicationsFreeBottom":"None",
   "PublicationsFreeTop":"<p><a title=\"Google Scholar Anna-Lena Lamprecht\" href=\"https://scholar.google.de/citations?user=d-GAM1oAAAAJ&amp;hl=de\" target=\"_blank\" rel=\"noopener\">Google Scholar</a> has a rather complete record of my publications, dating back to 2006. See below for research outputs since joining Utrecht University (June 2017).</p>\n<p>&nbsp;</p>",
   "Skills":[
      
   ],
   "State":"None",
   "StudyProgrammes":[
      {
         "Guid":"d1433cd0e7b44ddebce51fee6ddb213b",
         "Addition":"None",
         "FacultyId":"None",
         "Id":4235,
         "Name":"Business Informatics",
         "Url":"None"
      },
      {
         "Guid":"16cd2af6bf4d4f66ad9cc9a8579eff67",
         "Addition":"None",
         "FacultyId":"None",
         "Id":4236,
         "Name":"Computing Science",
         "Url":"None"
      },
      {
         "Guid":"bc28a2954357463ca9a6e802561baf59",
         "Addition":"None",
         "FacultyId":"None",
         "Id":4233,
         "Name":"Informatica",
         "Url":"None"
      },
      {
         "Guid":"c33ae14fef0241809ce655f88d6ec9c6",
         "Addition":"None",
         "FacultyId":"None",
         "Id":4234,
         "Name":"Informatiekunde",
         "Url":"None"
      }
   ],
   "Tabs":{
      "Guid":"2d8711878eb141a7927fde68fae1810b",
      "Activities":{
         "Guid":"47643a6177fe40da80bbcf92d7530a32",
         "Title":"Activiteiten",
         "Visible":true
      },
      "AdditionalFunctions":{
         "Guid":"7cb2a133ae1f4c3eac81e44bbd94ed90",
         "Title":"Nevenfuncties",
         "Visible":false
      },
      "Admin":{
         "Guid":"9afe8b533d4345a4b2fd6fc577e42184",
         "Title":"Beheer",
         "Visible":true
      },
      "CV":{
         "Guid":"79d603ae2e204f84b76ba9c5b8818a86",
         "Title":"CV",
         "Visible":true
      },
      "Contact":{
         "Guid":"3e82322480d3414d92dab443bcb8c4f3",
         "Title":"Contact",
         "Visible":true
      },
      "Courses":{
         "Guid":"136f5727aea84ab2a0c948998e595a09",
         "Title":"Onderwijs",
         "Visible":true
      },
      "CustomTab1":{
         "Guid":"aa58da75692d492483143c78991d8ae7",
         "Title":"",
         "Visible":false
      },
      "CustomTab2":{
         "Guid":"92d0b4ae0aea4ba08dc65194efce98cd",
         "Title":"",
         "Visible":false
      },
      "CustomTab3":{
         "Guid":"86826210e36b4e07b4b7eb79c000d891",
         "Title":"",
         "Visible":false
      },
      "CustomTabs":{
         "Guid":"5b5834c4ba8443c6b7122ce0d201617e",
         "Title":"Vrije pagina's",
         "Visible":true
      },
      "General":{
         "Guid":"e15255cdcd704e4da4a0b7eab5232557",
         "Title":"Algemeen",
         "Visible":true
      },
      "Help":{
         "Guid":"e6544c7a76c941af80fbe7a9dd199f7d",
         "Title":"Help",
         "Visible":true
      },
      "Media":{
         "Guid":"1714e8d08817443c92d5a412ba5314f0",
         "Title":"In de media",
         "Visible":false
      },
      "Prizes":{
         "Guid":"00b221a669a14dbcb6338f70fd35212f",
         "Title":"Prijzen",
         "Visible":true
      },
      "Profile":{
         "Guid":"e23ce4bd4fa543929be713d3d69df63e",
         "Title":"Profiel",
         "Visible":true
      },
      "Publications":{
         "Guid":"84a2e546ca414cc085fa0be5ae43d95d",
         "Title":"Publicaties",
         "Visible":true
      },
      "Research":{
         "Guid":"31f4bb8a959c4136b1a02a5b85466bcc",
         "Title":"Onderzoek",
         "Visible":true
      },
      "Statistics":{
         "Guid":"678669356e024ea3826ccdeb728dd16b",
         "Title":"Statistiek",
         "Visible":true
      }
   }
}

```

## Contact

This package was created by Class CoTaPP in a live coding session. Please contact Jonathan de Bruin for info j.debruin1@uu.nl. 
