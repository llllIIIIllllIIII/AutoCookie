import sqlite3
import pandas as pd


class save:
    resource_list = [
            ('RollCakeWood',1000,True),
            ('Jellybean',1000,True),
            ('SugarCube',1000,True),
            ('BiscuitFlour',1000,True),
            ('Jellyberry',1000,True),
            ('Milk',500,True),
            ('CottonCandyWool',300,True),
            ('RobustAxe',100,False),
            ('TemperedPickaxe',60,False),
            ('CandySaw',60,False),
            ('DiggyShovel',60,False),
            ('EnchantedTongs',60,False),
            ('IndestructibleGlazedHammer',68,False),
            ('JellybeanJam',60,False),
            ('SweetJellyJam',60,False),
            ('ToffeeJam',60,False),
            ('Pomegranate',0,False),
            ('Sparkleberry',0,False),
            ('PineconeBirdyToy',80,False),
            ('AcornLamp',80,False),
            ('CuckooClock',40,False),
            ('SwanFeatherDreamcatcher',0,False),
            ('HeartyRye',40,False),
            ('TartJampie',30,False),
            ('GinkgoFocaccia',40,False),
            ('GlazedDonuts',40,False),
            ('FluffyCastella',20,False),
            ('GoldenCroissant',0,False),
            ('HotJellyStew',60,False),
            ('BearJellyBurger',60,False),
            ('CandyPasta',40,False),
            ('FluffyOmurice',0,False),
            ('JellyDeluxePizza',0,False),
            ('FancyJellybeanMeal',0,False),
            ('BiscuitPlanter',60,False),
            ('ShinyGlass',60,False),
            ('GleamyBead',0,False),
            ('ColorfulBowl',0,False),
            ('CandyFlower',60,False),
            ('HappyPlanter',60,False),
            ('CandyBouquet',40,False),
            ('LollipopFlowerBasket',20,False),
            ('Bell-FlowerBouquet',0,False),
            ('GlitteringYogurtWreath',0,False),
            ('Cream',60,False),
            ('Butter',0,False),
            ('HomemadeCheese',0,False),
            ('JellybeanLatte',80,False),
            ('BubblyBoba',20,False),
            ('SweetberryJuice',0,False),
            ('CloudPillow',100,False),
            ('BearJellyToy',20,False),
            ('PitayaDragonToy',0,False),
            ('CreamRootBeer',60,False),
            ('RedberryJuice',20,False),
            ('VintageRootBottle',20,False),
            ('SpookyMuffin',20,False),
            ('StrawberryCake',0,False),
            ('PartyCake',0,False),
            ('GlazedRing',100,False),
            ('RubyberryBrooch',0,False),
            ('BearJellyCrown',0,False)
        ]
    conn = sqlite3.connect('Resource.db',check_same_thread=False)
    c = conn.cursor()
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    def __init__(self):
        
        self.c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='resource_table' ''')
        if self.c.fetchone()[0]!=1 :
            print("""not exsist""")
            self.c.execute("""CREATE TABLE IF NOT EXISTS resource_table (
                            resource_name text,
                            resource_limit integer,
                            is_meterial blob
                            )""")
            self.c.executemany('INSERT INTO resource_table VALUES(?,?,?);', self.resource_list)                    
        self.conn.commit()

    #Update Resource Limit
    def update(self,ResourceName,new_limit):
        self.c.execute(""" UPDATE resource_table SET resource_limit = ?
        WHERE resource_name = ? """
        ,(new_limit,ResourceName))
        self.conn.commit()

    #Select specific resource
    def limit(self,resourceName):
        self.c.execute(' SELECT * FROM resource_table WHERE resource_name = ?',(resourceName,))   
        a =  self.c.fetchone()
        return a[1]
    

    #Check if is meterial
    def is_metirial(self,resourceName):
        self.c.execute(' SELECT * FROM resource_table WHERE resource_name = ?',(resourceName,))
        a = self.c.fetchone()
        return a[2]

    #List all resource
    def list_all(self):
        l = []
        self.c.execute("SELECT * FROM resource_table")
        items = self.c.fetchall()
        for item in items:
            a,b,_ = item
            c = (a,b)
            l.append(c)
        df = pd.DataFrame(l,columns=['名稱',' 上限 '])
        return df

    #Close Database
    def close(self):
        self.conn.close()
    










