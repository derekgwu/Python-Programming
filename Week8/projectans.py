import copy


"""```````````````````````````````YOUR FUNCTIONS```````````````````````````````"""

"""```Milestone 0```"""
def data_clean(data, src):
    datatype = "" 
    #Cleans out tabs
    src = src.replace("\t", " ")

    #puts each string into the array
    for i in range(0, len(src), 1):
        if src[i] == '\n':
            data.append(datatype)
            datatype = ""
        else:
            datatype = datatype + src[i]
    
    return data


"""```Milestone 1```"""
def year_parse(data):
    string = ""
    tracker = []
    for entry in data:
        string = entry[len(entry) - 4 :len(entry)]
        ret = search(tracker, int(string))
        if ret == False:
            tracker.append(int(string))
            tracker.sort()
    return tracker

def keyword_search(data, keyword):
    for entry in data:
        if keyword in entry:
            return entry
        
    return ""

def most_popular_franchise(data):
    tracker = [
        ["Mario", 0],
        ["Grand Theft Auto", 0],
        ["Pokemon", 0],
        ["Call of Duty", 0],
        ["The Witcher", 0],
        ["Zelda", 0],
    ]

    for entry in data:
        for i in range(0, len(tracker), 1):
            if tracker[i][0] in entry:
                tracker[i][1] += 1
    return tracker

"""```Milestone 2```"""
def sort_by_year(data):
    new_data = copy.deepcopy(data)
    new_data.sort(key=get_year)
    return new_data


def your_own_func():
    return

    
"""```````````````````````````````HELPER FUNCTIONS```````````````````````````````"""
"""DO NOT EDIT ANYTHING HERE"""
#helper functions! you can use these whenever you need to


def search(tracker, entry):
    for x in tracker:
        if entry == x:
            return True
    return False

def get_year(entry):
    return int(entry[len(entry) - 4 :len(entry)])


"""```````````````````````````````UNIT TESTS```````````````````````````````"""
"""DO NOT EDIT ANYTHING HERE"""
#Unit Tests
#The asserter
def asserter(test_case, exp, ret, exception):
    if(exception == True):
        print("Test Case " + str(test_case) + " had an exception")
        return 0
    if(exp == ret):
        print("Test Case " + str(test_case) + " SUCCESS!")
        return 1
    else:
        print("Test Case " + str(test_case) + " FAILED. We expected: " + str(exp) + " but you returned " + str(ret))
        return 0

#all the tests for milestone 0
def m0_tests(data):
    print("Starting Milestone 0 Unit Tests:")
    #tests the formatting of the first entry
    m0_tests_passed = 0
    try:
        ans = "Minecraft |300,000,000| Minecraft Multi-platform November 18, 2011"
        m0_tests_passed += asserter(1, ans, data[0], False)
    except:
        m0_tests_passed += asserter(1, 0, 0, True)
    
    if m0_tests_passed == 1:
        print("\nMilestone 0 Passed!")
    else:
        print("\nMilestone 0 Tests Passed: " + str(m0_tests_passed) + "/1")
       
def m1_tests(data, year_tracker, franchise_tracker):
    print("Starting Milestone 1 Unit Tests:")
    tests_m1_passed = 0
    print("\n")
    #tests the year parse and asserts the year tracker is sorted by year
    exp_arr = [1980, 1984, 1985, 1988, 1989, 1990, 1991, 1996, 1999, 2002, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    check = True
    tests_m1_passed += asserter(1, exp_arr, year_tracker, False)

    #checks your game search
    tests_m1_passed += asserter(2.1, "Wii Sports |82,900,000| Wii Wii November 19, 2006", keyword_search(data, "Wii Sports"), False)
    tests_m1_passed += asserter(2.2, "", keyword_search(data, "Fortnite"), False)
    tests_m1_passed += asserter(2.3, "Mario Kart 8 / Deluxe |63,920,000| Mario Kart Wii U / Switch May 29, 2014", keyword_search(data, "Mario Kart"), False)

    #checks your franchise tracker
    exp_arr = [['Mario', 10], ['Grand Theft Auto', 3], ['Pokemon', 6], ['Call of Duty', 4], ['The Witcher', 1], ['Zelda', 1]] 
    tests_m1_passed += asserter(3, exp_arr, franchise_tracker, False)

    if tests_m1_passed == 5:
        print("\nMilestone 1 Passed!")
    else:
        print("\nMilestone 1 Tests Passed: " + str(tests_m1_passed) + "/5")

def m2_tests(data):
    print("Starting Milestone 2 Unit Tests:\n")
    exp = ['Pac-Man |42,071,635| Pac-Man Multi-platform May 22, 1980', 'Duck Hunt |28,300,000| None NES April 21, 1984', 'Super Mario Bros. |58,000,000| Super Mario Multi-platform September 13, 1985', 'Super Mario Bros. 3 |24,430,000| Super Mario Multi-platform October 23, 1988', 'Tetris (1989)[f] |48,000,000| Tetris Game Boy / NES June 14, 1989', 'Super Mario World |26,662,500| Super Mario Multi-platform November 21, 1990', 'Sonic the Hedgehog |23,482,960| Sonic the Hedgehog Multi-platform June 23, 1991', 'Pokemon Red / Green / Blue / Yellow |47,520,000| Pokemon Multi-platform February 27, 1996', 'Pokemon Gold / Silver / Crystal |29,490,000| Pokemon Game Boy Color November 21, 1999', 'Pokemon Ruby / Sapphire / Emerald |23,280,000| Pokemon Game Boy Advance November 21, 2002', 'Grand Theft Auto: San Andreas |27,500,000| Grand Theft Auto Multi-platform October 26, 2004', 'Nintendogs |23,960,000| None Nintendo DS April 21, 2005', 'Mario Kart DS |23,600,000| Mario Kart Nintendo DS November 14, 2005', 'Tetris (EA) |100,000,000| Tetris Multi-platform September 12, 2006', 'Wii Sports |82,900,000| Wii Wii November 19, 2006', 'New Super Mario Bros. |30,800,000| Super Mario Nintendo DS May 15, 2006', 'Wii Play |28,020,000| Wii Wii December 2, 2006', 'Pokemon Diamond / Pearl / Platinum |24,730,000| Pokemon Nintendo DS September 28, 2006', 'Wii Fit / Plus |43,800,000| Wii Wii December 1, 2007', 'Mario Kart Wii |37,380,000| Mario Kart Wii April 10, 2008', 'Grand Theft Auto IV |27,750,000| Grand Theft Auto Multi-platform April 29, 2008', 'Wii Sports Resort |33,140,000| Wii Wii June 25, 2009', 'New Super Mario Bros. Wii |30,320,000| Super Mario Wii November 11, 2009', 'Call of Duty: Black Ops |26,200,000| Call of Duty Multi-platform November 9, 2010', 'Kinect Adventures! |24,000,000| None Xbox 360 November 4, 2010', 'Minecraft |300,000,000| Minecraft Multi-platform November 18, 2011', 'Terraria |44,500,000| None Multi-platform May 16, 2011', 'Call of Duty: Modern Warfare 3 |26,500,000| Call of Duty Multi-platform November 8, 2011', 'Diablo III |29,750,000| Diablo Multi-platform May 16, 2012', 'The Walking Dead |28,000,000| The Walking Dead Multi-platform April 24, 2012', 'Borderlands 2 |27,000,000| Borderlands Multi-platform September 18, 2012', 'New Super Mario Bros. U / Luigi U / Deluxe  |25,060,000| Super Mario Wii U / Switch November 18, 2012', 'Call of Duty: Black Ops II |24,200,000| Call of Duty Multi-platform November 12, 2012', 'Grand Theft Auto V |185,000,000| Grand Theft Auto Multi-platform September 17, 2013', 'Mario Kart 8 / Deluxe |63,920,000| Mario Kart Wii U / Switch May 29, 2014', 'The Witcher 3: Wild Hunt |50,000,000| The Witcher Multi-platform May 19, 2015', 'Overwatch |50,000,000| Overwatch Multi-platform May 24, 2016', 'Human: Fall Flat |40,000,000| None Multi-platform July 22, 2016', 'Pokemon Sun / Moon / Ultra Sun / Ultra Moon |25,450,000| Pokemon Nintendo 3DS November 18, 2016', 'PUBG: Battlegrounds |75,000,000| PUBG Universe Multi-platform December 20, 2017', 'The Legend of Zelda: Breath of the Wild |32,350,000| The Legend of Zelda Wii U / Switch March 3, 2017', 'Super Mario Odyssey |26,440,000| Super Mario Nintendo Switch October 27, 2017', 'FIFA 18 |26,400,000| FIFA Multi-platform September 29, 2017', 'Red Dead Redemption 2 |55,000,000| Red Dead Multi-platform October 26, 2018', 'Super Smash Bros. Ultimate |31,770,000| Super Smash Bros. Nintendo Switch December 7, 2018', 'God of War |23,000,000| God of War PlayStation 4 / Windows April 20, 2018', 'Call of Duty: Modern Warfare |30,000,000| Call of Duty Multi-platform October 25, 2019', 'Pokemon Sword / Shield |25,920,000| Pokemon Nintendo Switch November 15, 2019', 'Animal Crossing: New Horizons |42,790,000| Animal Crossing Nintendo Switch March 20, 2020', 'Cyberpunk 2077 |25,000,000| Cyberpunk Multi-platform December 10, 2020']
    m2_tests_passed = 0
    
    m2_tests_passed += asserter(1, exp, sort_by_year(data), False)
    if m2_tests_passed == 1:
        print("Milestone 2 Passed!")
    else:
        print("\nMilestone 2 Tests Passed: " + str(m2_tests_passed) + "/1")
"""```````````````````````````````MAIN FUNCTION```````````````````````````````"""
"""DO NOT EDIT ANYTHING HERE"""
file = open(r'\Users\dchen\Desktop\CompSci\tutoring-files\Week8\data.txt')
src = file.read()
data = []

#Milestone 0
data_clean(data, src)

#Milestone 1

year_tracker = year_parse(data)



franchise_tracker = most_popular_franchise(data)

sort_by_year(data)



"""```````````````````````````````UNIT TESTING CALLS```````````````````````````````"""
"""DO NOT EDIT ANYTHING HERE"""
run_m0 = True
run_m1 = True
run_m2 = True
if run_m0 == True:
    m0_tests(data)

if run_m1 == True:
    m1_tests(data, year_tracker, franchise_tracker)

if run_m2 == True:
    m2_tests(data)



