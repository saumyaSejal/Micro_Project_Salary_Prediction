import numpy as np
import pickle 
import streamlit as st
model=pickle.load(open('svr_model.sav','rb'))

#creating a function for prediction 

#def salary_prediction(input_data):



def main():

    #url of the website  
    st.header("Microprocessor Project",divider='grey')
    st.title('Salary Prediction')

    #user data 
    # Job Title', 'Rating', 'Company Name', 'Location', 'Size',
    #    'Type of ownership', 'Industry', 'Sector', 'Revenue', 'python_yn',
    #    'R_yn', 'spark', 'aws', 'excel'
    
    job_title=st.selectbox(('Choose your job title'),('Data Scientist',
 'Healthcare Data Scientist',
 'Research Scientist',
 'Staff Data Scientist - Technology',
 'Data Analyst',
 'Data Engineer I',
 'Scientist I/II, Biology',
 'Customer Data Scientist',
 'Data Scientist - Health Data Analytics',
 'Senior Data Scientist / Machine Learning',
 'Data Scientist - Quantitative',
 'Digital Health Data Scientist',
 'Associate Data Analyst',
 'Clinical Data Scientist',
 'Data Scientist / Machine Learning Expert',
 'Web Data Analyst',
 'Senior Data Scientist',
 'Data Engineer',
 'Data Scientist - Algorithms & Inference',
 'Scientist',
 'Lead Data Scientist',
 'Spectral Scientist/Engineer',
 'College Hire - Data Scientist - Open to December 2019 Graduates',
 'Data Scientist, Office of Data Science',
 'Data Science Analyst',
 'Data Scientist (Warehouse Automation)',
 'Jr. Data Scientist',
 'Data Architect / Data Modeler',
 'Associate Scientist / Sr. Associate Scientist, Antibody Discovery',
 'Machine Learning Engineer (NLP)'))
    
    rating=st.number_input('Enter Rating')
    company_name=st.selectbox(('Choose Companies Name'),(('Tecolote Researc',
 'University of Maryland Medical Syste',
 'KnowBe',
 'PNN',
 'Affinity Solution',
 'CyrusOn',
 'ClearOne Advantag',
 'Logic20/2',
 'Rochester Regional Healt',
 '<intent',
 'Wis',
 'ManTec',
 'Walmar',
 'Yesle',
 'Takeda Pharmaceutical',
 'Audibl',
 'Blueprint Medicine',
 'h2o.a',
 'Nun',
 'Pinnacol Assuranc',
 'Porc',
 'Health I',
 'Truckstop.co',
 'SMC ',
 'Novett',
 'Pfize',
 'First Tech Federal Credit Unio',
 'The Hanover Insurance Grou',
 'Amroc',
 'Novarti',
 'Juniper Network',
 'New England Biolab',
 'Clarity Insight',
 'Esr',
 'Systems & Technology Researc',
 'Sartoriu',
 'Lancer Insuranc',
 'Sauce Lab',
 'Persivi',
 'Edgewell Personal Car',
 'Equity Residentia',
 'BPA Service',
 'Visa Inc',
 'Intrad',
 'Centaur',
 'Caterpilla',
 'Zimmerman Advertisin',
 'Liberty Mutual Insuranc',
 'Torch Technologies, Inc',
 'Swiss R',
 'Northrop Grumma',
 'Netskop',
 '1904lab',
 'The David J. Joseph Compan',
 'USERead',
 'Bill.co',
 'Pacific Northwest National Laborator',
 "DICK'S Sporting Goods - Corporat",
 'Berg Healt',
 'Oversight System',
 'C Spac',
 'Numeric, LL',
 'HP Inc',
 'SpringM',
 'Grainge',
 'EAG Laboratorie',
 'The Buffalo Grou',
 'Carmeus',
 'GNS Healthcar',
 'Perato',
 'Pacter',
 'Nur',
 'webfx.co',
 'Johns Hopkins University Applied Physics Laborator',
 'Productive Edg',
 'Excella Consultin',
 'Gensc',
 'goTR',
 'NMR Consultin',
 'iSeat',
 'Nektar Therapeutic',
 'TransUnio',
 'IT Concept',
 'Scientific Research Corporatio',
 'General Dynamics Information Technolog',
 'MITR',
 'DentaQues',
 'Redjac',
 '7Park Dat',
 'Rapid Response Monitorin',
 'Trilogy E',
 'Gallu',
 'CapTec',
 'American Axle & Manufacturin',
 'CentralReac',
 'Integrat',
 'Boys Town Hospita',
 'Demandbas',
 'Sapphire Digita',
 'Formatio',
 'Autodes',
 "Beck's Hybrid",
 'DrFirs',
 'Object Partner',
 'L.A. Care Health Pla',
 'Red Venture',
 'Quick Bas',
 'The E.W. Scripps Compan',
 'Upside Business Trave',
 'Synagr',
 'Alliance Source Testin',
 'Accuride Internationa',
 'Full Potential Solution',
 'Maven Wave Partner',
 'First Command Financial Services, Inc',
 'Pharmavit',
 'BioMarin Pharmaceutica',
 'Stratagem Grou',
 'PA Consultin',
 'Gridiron I',
 'Evolve Vacation Renta',
 'The Church of Jesus Christ of Latter-day Saint',
 'Maximus Real Estate Partner',
 'Software Engineering Institut',
 'AVANAD',
 'PatientPoin',
 'BlueCross BlueShield of Tennesse',
 'KSM Consultin',
 'Cogo Lab',
 'Church & Dwigh',
 'MassMutua',
 'Genentec',
 'Legal & General Americ',
 'Western Digita',
 'Sunovio',
 'National Student Clearinghous',
 'Tower Healt',
 'State of Wisconsin Investment Boar',
 'Rubius Therapeutic',
 'OneMagnif',
 'IZE',
 'Vionic Grou',
 'Dodge Data & Analytic',
 'Plymouth Rock Assuranc',
 'CA-One Tech ',
 'Beebe Healthcar',
 'Argo Group U',
 'Associated Electric Cooperativ',
 'PennyMa',
 'Zest A',
 'DECISIVE ANALYTICS Corporatio',
 'Karyopharm Therapeutics Inc',
 'Tempus Lab',
 'Recursion Pharmaceutical',
 'P2 Energy Solution',
 'ClearEdg',
 'Tapjo',
 'Credit Sesam',
 'San Manuel Casin',
 'Texas Health Huguley Hospita',
 'Teasdale Latin Food',
 'Central California Alliance for Healt',
 'Pilot Flying J Travel Centers LL',
 "Palermo's Pizz",
 'Advanced BioScience Laboratorie',
 'Echo Global Logistic',
 'Lockheed Marti',
 'Acuity Insuranc',
 'Fareporta',
 'Veterans Affairs, Veterans Health Administratio',
 'Creder',
 'Spectrum Communications and Consultin',
 'NCSOF',
 'Dayton Freight Lines, Inc',
 'Community Action Partnership of San Luis Obisp',
 'TrueAccor',
 'DRB System',
 'Corcentri',
 'U.Grou',
 'Systems Evolution Inc',
 'Eventbrit',
 'Centr',
 'comScor',
 'SullivanCotte',
 'NP',
 'Bakery Agenc',
 'Blue Cross & Blue Shield of Rhode Islan',
 'Boys Tow',
 'The HSC Health Care Syste',
 'Pro-Sphere Te',
 'Ameritas Life Insurance Cor',
 'Genwort',
 'Trace Dat',
 'Clearwater Analytic',
 'Tekvalley, Corp',
 'BWX Technologie',
 'Vermee',
 'L&T Infotec',
 'OceanFirst Financia',
 "Sotheby'",
 'Vanda Pharmaceutical',
 'CK-12 Foundatio',
 'Opinion Dynamic',
 'Applied Information Science',
 'WK Dickso',
 'Southwest Research Institut',
 'Mus',
 'The Integer Grou',
 'Samba T',
 'SV Microwav',
 'Sumo Logi',
 'EA',
 'Brighthouse Financia',
 'Citadel Federal Credit Unio',
 'CALIBRE System',
 'Motorola Solution',
 'Reynolds America',
 'Infosy',
 'Alignment Healthcar',
 'Cboe Global Market',
 'Guidepoin',
 'Cerus Corporatio',
 'Vail Healt',
 'AstraZenec',
 'MathWork',
 'MetroStar System',
 'Audentes Therapeutic',
 'National Interstat',
 'Moser Consultin',
 'Mcphail Associate',
 'Crown Bioscienc',
 'HOVE',
 'Q2 Solution',
 'Arbella Insuranc',
 'Krono',
 'Associated Banc-Cor',
 'Genesy',
 'Moda Operand',
 'Q',
 'Santande',
 'Tivity Healt',
 'BRM',
 'Luminar Technologie',
 'Emtec, Inc',
 'Veterans United Home Loan',
 'Praetoria',
 'Agios Pharmaceutical',
 'Glassdoo',
 'Assuran',
 'F&',
 'GreatAmerica Financial Service',
 'Acceleron Pharm',
 'AmeriHealth Carita',
 'Strategic Employment Partner',
 'Catholic Health Initiative',
 'FLEETCO',
 'Applied Research Laboratorie',
 'Raytheo',
 'RTI Internationa',
 'TRANZAC',
 'United BioSourc',
 'Figure Eigh',
 'Royce Geospatia',
 'Cit',
 'Sage Intacc',
 'Scale A',
 'Change Healthcar',
 'M',
 'HG Insight',
 '1-800-FLOWERS.COM, Inc',
 'CBS Interactiv',
 'Samsung Research Americ',
 'Lorven Technologies In',
 'CareD',
 'Serigor Inc',
 'Leido',
 'Beckman Coulter Diagnostic',
 'IHS Marki',
 'ALI',
 'e-IT Professionals Corp',
 'TechProject',
 'Biz2Credit In',
 'PeoplesBan',
 'Capgemin',
 'GNY Insurance Companie',
 'Conch Technologies, In',
 'Medidata Solution',
 'Quartet Healt',
 'Success Academy Charter School',
 'AXION Healthcare Solution',
 'ExecOnlin',
 'Mte',
 'Brillien',
 'Entef',
 'Trace',
 'Saama Technologies In',
 'Two Sigm',
 'Strategic Financial Solution',
 'Remedy BPCI Partners, LLC',
 'The Climate Corporatio',
 'Crossix Solution',
 'GS',
 'Factua',
 'TriNe',
 'Signpos',
 'Adob',
 'Equian LL',
 'Information Builder',
 'Greenway Healt',
 'Confluen',
 'Life36',
 'IQVI',
 'Riverside Research Institut',
 'Icon Health and Fitnes',
 'Ship',
 'Monte Rosa Therape',
 'IntraEdg',
 'COUNTRY Financia',
 'Mentor Graphic',
 'Maxar Technologie',
 'ICW Grou',
 'Exelixi',
 'Grand Round',
 'SPINS, LL',
 'DTC',
 'Carilion Clini',
 'DoubleVerif',
 'Mitsubishi Electric Research Lab',
 'Rodan and Fields, LL',
 'DES',
 'Johns Hopkins Health Car',
 'Community Behavioral Healt',
 'FORMA THERAPEUTIC',
 'Brid',
 'Charter Spectru',
 'CompQsof',
 'Solugenix Corporatio',
 'West Coast Universit',
 'SoftBank Robotic',
 'SkySyn',
 'DatamanUSA, LL',
 '23andM',
 'Fivestar')))
    location=st.selectbox(('choose your location'),('Albuquerque, NM',
 'Linthicum, MD',
 'Clearwater, FL',
 'Richland, WA',
 'New York, NY',
 'Dallas, TX',
 'Baltimore, MD',
 'San Jose, CA',
 'Rochester, NY',
 'Chantilly, VA',
 'Plano, TX',
 'Seattle, WA',
 'Cambridge, MA',
 'Newark, NJ',
 'Mountain View, CA',
 'San Francisco, CA',
 'Denver, CO',
 'Chicago, IL',
 'Louisville, KY',
 'Herndon, VA',
 'Hillsboro, OR',
 'Worcester, MA',
 'Groton, CT',
 'Detroit, MI',
 'Sunnyvale, CA',
 'Ipswich, MA',
 'Redlands, CA',
 'Woburn, MA',
 'Fremont, CA',
 'Long Beach, NY',
 'Marlborough, MA',
 'Allendale, NJ',
 'Washington, DC',
 'Bellevue, WA',
 'Longmont, CO',
 'Beavercreek, OH',
 'Peoria, IL',
 'Fort Lauderdale, FL',
 'Boston, MA',
 'Huntsville, AL',
 'Armonk, NY',
 'San Diego, CA',
 'Saint Louis, MO',
 'Cincinnati, OH',
 'Palo Alto, CA',
 'Coraopolis, PA',
 'Framingham, MA',
 'Atlanta, GA',
 'Philadelphia, PA',
 'Vancouver, WA',
 'Indianapolis, IN',
 'Lake Forest, IL',
 'Maryland Heights, MO',
 'Charlottesville, VA',
 'Pittsburgh, PA',
 'Harrisburg, PA',
 'Laurel, MD',
 'Arlington, VA',
 'Tacoma, WA',
 'Miami, FL',
 'New Orleans, LA',
 'Landover, MD',
 'Patuxent River, MD',
 'Suitland, MD',
 'McLean, VA',
 'Fort Belvoir, VA',
 'Milwaukee, WI',
 'Silver Spring, MD',
 'Syracuse, NY',
 'Houston, TX',
 'Charlotte, NC',
 'Southfield, MI',
 'Matawan, NJ',
 'Phoenix, AZ',
 'Omaha, NE',
 'Lyndhurst, NJ',
 'Atlanta, IN',
 'Rockville, MD',
 'Minneapolis, MN',
 'Los Angeles, CA',
 'Alabaster, AL',
 'Santa Fe Springs, Los Angeles, CA',
 'Kansas City, MO',
 'Ashburn, VA',
 'Fort Worth, TX',
 'Valencia, CA',
 'Novato, CA',
 'Aurora, CO',
 'Tampa, FL',
 'Riverton, UT',
 'Chattanooga, TN',
 'Ewing, NJ',
 'South San Francisco, CA',
 'Cupertino, CA',
 'Frederick, MD',
 'West Reading, PA',
 'Madison, WI',
 'Dearborn, MI',
 'Winter Park, FL',
 'San Rafael, CA',
 'Hamilton, NJ',
 'Woodbridge, NJ',
 'Lewes, DE',
 'Springfield, MO',
 'Burbank, CA',
 'Newton, MA',
 'Salt Lake City, UT',
 'Lafayette, LA',
 'Annapolis Junction, MD',
 'Highland, CA',
 'Burleson, TX',
 'Hoopeston, IL',
 'Scotts Valley, CA',
 'Knoxville, TN',
 'Millville, DE',
 'Sheboygan, WI',
 'San Mateo, CA',
 'Dayton, OH',
 'Parlier, CA',
 'Meridian, ID',
 'Cherry Hill, NJ',
 'Nashville, TN',
 'Portland, OR',
 'Port Washington, NY',
 'Austin, TX',
 'Providence, RI',
 'Raleigh, NC',
 'Phila, PA',
 'Oakland, CA',
 'Boise, ID',
 'Oak Ridge, TN',
 'Agoura Hills, CA',
 'Pella, IA',
 'San Ramon, CA',
 'Red Bank, NJ',
 'Columbia, SC',
 'Springfield, MA',
 'San Antonio, TX',
 'Portsmouth, VA',
 'West Palm Beach, FL',
 'Exton, PA',
 'Alexandria, VA',
 'Owensboro, KY',
 'Hartford, CT',
 'Orange, CA',
 'Lenexa, KS',
 'Concord, CA',
 'Vail, CO',
 'Natick, MA',
 'Winston-Salem, NC',
 'Richfield, OH',
 'Hampton, VA',
 'Ithaca, NY',
 'Marietta, GA',
 'Quincy, MA',
 'Green Bay, WI',
 'Durham, NC',
 'Clovis, CA',
 'Chandler, AZ',
 'Orlando, FL',
 'Columbia, MO',
 'Westlake, OH',
 'Des Moines, IA',
 'Cedar Rapids, IA',
 'Fort Lee, NJ',
 'Blue Bell, PA',
 'Springfield, VA',
 'Jersey City, NJ',
 'Emeryville, CA',
 'Santa Barbara, CA',
 'Carle Place, NY',
 'King of Prussia, PA',
 'Santa Clara, CA',
 'Brisbane, CA',
 'Foster City, CA',
 'Holyoke, MA',
 'Waltham, MA',
 'Corvallis, OR',
 'Gaithersburg, MD',
 'Bedford, MA',
 'Aliso Viejo, CA',
 'Dublin, CA',
 'Arvada, CO',
 'Franklin, TN',
 'Plymouth Meeting, PA',
 'Allentown, PA',
 'Logan, UT',
 'Birmingham, AL',
 'Reston, VA',
 'Scottsdale, AZ',
 'Bloomington, IL',
 'Alameda, CA',
 'Roanoke, VA',
 'Glen Burnie, MD',
 'Milpitas, CA',
 'Watertown, MA',
 'Cambridge, MD',
 'Irvine, CA',
 'Ann Arbor, MI',
 'Olympia, WA'))
    
    size=st.number_input("enter size of the company")
    ownership=st.selectbox(("type of ownership"),('Company - Private',
 'Other Organization',
 'Government',
 'Company - Public',
 'Hospital',
 'Subsidiary or Business Segment',
 'Nonprofit Organization',
 'Unknown',
 'College / University',
 'School / School District',
 '-1'))
    
    industry=st.selectbox(("choose the type of industry"),('Aerospace & Defense',
 'Health Care Services & Hospitals',
 'Security Services',
 'Energy',
 'Advertising & Marketing',
 'Real Estate',
 'Banks & Credit Unions',
 'Consulting',
 'Internet',
 'Other Retail Stores',
 'Research & Development',
 'Department, Clothing, & Shoe Stores',
 'Biotech & Pharmaceuticals',
 'Motion Picture Production & Distribution',
 'Enterprise Software & Network Solutions',
 'Insurance Carriers',
 'Insurance Agencies & Brokerages',
 'Logistics & Supply Chain',
 'Telecommunications Services',
 'IT Services',
 'Computer Hardware & Software',
 '-1',
 'Consumer Products Manufacturing',
 'Industrial Manufacturing',
 'Metals Brokers',
 'Financial Transaction Processing',
 'Sporting Goods Stores',
 'Staffing & Outsourcing',
 'Wholesale',
 'Mining',
 'Financial Analytics & Research',
 'Federal Agencies',
 'Education Training Services',
 'Transportation Equipment Manufacturing',
 'Farm Support Services',
 'TV Broadcast & Cable Networks',
 'Architectural & Engineering Services',
 'Brokerage Services',
 'Travel Agencies',
 'Religious Organizations',
 'Colleges & Universities',
 'Investment Banking & Asset Management',
 'Lending',
 'Gambling',
 'Food & Beverage Manufacturing',
 'Gas Stations',
 'Transportation Management',
 'Video Games',
 'Trucking',
 'Social Assistance',
 'Auctions & Galleries',
 'K-12 Education',
 'Telecommunications Manufacturing',
 'Stock Exchanges',
 'Construction',
 'Accounting',
 'Health Care Products Manufacturing',
 'Health, Beauty, & Fitness',
 'Consumer Product Rental',
 'Beauty & Personal Accessories Stores'))


    ector=st.selectbox(('choose sector'),('Aerospace & Defense',
 'Health Care',
 'Business Services',
 'Oil, Gas, Energy & Utilities',
 'Real Estate',
 'Finance',
 'Information Technology',
 'Retail',
 'Biotech & Pharmaceuticals',
 'Media',
 'Insurance',
 'Transportation & Logistics',
 'Telecommunications',
 '-1',
 'Manufacturing',
 'Mining & Metals',
 'Government',
 'Education',
 'Agriculture & Forestry',
 'Travel & Tourism',
 'Non-Profit',
 'Arts, Entertainment & Recreation',
 'Construction, Repair & Maintenance',
 'Accounting & Legal',
 'Consumer Services'))

    revenue=st.text_input('enter revenue of the company')

    
    col1,col2,col3,col4,col5=st.columns(5)
    col1.checkbox("python") 
    col2.checkbox("R")
    col3.checkbox("aws")
    col4.checkbox("spark")
    col5.checkbox("excel")
    
    st.button("Predict the Salary")
    
   
if __name__ == '__main__':
    main()
