import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 749))

background = pygame.image.load(r'C:\Users\jessi\Downloads\space(resized).jpg')
astronaut = pygame.image.load(r'C:\Users\jessi\Downloads\character(small).png')
name = pygame.image.load(r'C:\Users\jessi\Downloads\astronaut.png')
mercury = pygame.image.load(r'C:\Users\jessi\Downloads\mercury.png')
venus = pygame.image.load(r'C:\Users\jessi\Downloads\venus.png')
earth = pygame.image.load(r'C:\Users\jessi\Downloads\earth.png')
mars = pygame.image.load(r'C:\Users\jessi\Downloads\mars.png')
jupiter = pygame.image.load(r'C:\Users\jessi\Downloads\jupiter.png')
saturn = pygame.image.load(r'C:\Users\jessi\Downloads\saturn.png')
uranus = pygame.image.load(r'C:\Users\jessi\Downloads\uranus.png')
neptune = pygame.image.load(r'C:\Users\jessi\Downloads\neptune.png')

bigmercury = pygame.image.load(r'C:\Users\jessi\Downloads\image0 (5).png')
bigvenus = pygame.image.load(r'C:\Users\jessi\Downloads\image0 (3).png')
bigearth = pygame.image.load(r'C:\Users\jessi\Downloads\image0 (8).png')
bigmars = pygame.image.load(r'C:\Users\jessi\Downloads\image0 (1).png')
bigjupiter = pygame.image.load(r'C:\Users\jessi\Downloads\image0 (2).png')
bigsaturn = pygame.image.load(r'C:\Users\jessi\Downloads\image0 (7).png')
biguranus = pygame.image.load(r'C:\Users\jessi\Downloads\image0 (6).png')
bigneptune = pygame.image.load(r'C:\Users\jessi\Downloads\image0 (4).png')

gameFinished = False
beginning = True
tutorial = False
loading = False
success = False
fail = False

qmercury = False
qvenus = False
qearth = False
qmars = False
qjupiter = False
qsaturn = False
quranus = False
qneptune = False

white = (255, 255, 255)

myFont = pygame.font.SysFont("Times New Roman", 30)
start = myFont.render("Start?", 1, white)
learn = myFont.render("Tutorial?", 1, white)
title = myFont.render("A Spacewalk Home", 1, white)
incorrect = myFont.render("Wrong!", 1, white)
correct = myFont.render("Correct!", 1, white)

dmercury = myFont.render("Mercury is the smallest planet in the Solar System and the closest to the Sun.", 1, white)
dmercury1 = myFont.render("The proximity of Mercury to the sun makes it the second hottest planet.", 1, white)
dmercury2 = myFont.render("Hence, making it inhabitable for humans", 1, white)
dvenus = myFont.render("As the second planet in the solar system,", 1, white)
dvenus1 = myFont.render("it's surface tempereture is hot enough to melt lead with a melting point of 327.5°C.", 1, white)
dvenus2 = myFont.render("In addition, the atmosphere is 90 times thicker then earth making it unhabitable.", 1, white)
dmars = myFont.render("Mars is named after the Roman god of war.", 1, white)
dmars1 = myFont.render("It is also the fourth planet from the Sun", 1, white)
dmars2 = myFont.render("and the second smallest planet in the solar system.", 1, white)
dmars3 = myFont.render("There have been many attempts to see if Mars is habitable through rovers.", 1, white)
djupiter = myFont.render("Jupiter is a gas giant composed of many toxic gases,", 1, white)
djupiter1 = myFont.render("it is also very distanced from the sun making it unhabitable for humans right now.", 1, white)
dsaturn = myFont.render("Saturn is a gas giant that is also extremely cold making it inhabitable for humans.", 1, white)
duranus = myFont.render ("Uranus is a gas giant composed of many toxic gases.", 1, white)
duranus1 = myFont.render("In the meantime, the pressure within the planet is huge, making it unhabitable. ", 1, white)
dneptune = myFont.render("The temperature of Neptune is extremely cold,", 1, white)
dneptune1 = myFont.render("making it impossible for liquid water to exist.", 1, white)
dneptune2 = myFont.render("Therefore, it is impossible for humans to live there right now.", 1, white)
dearth = myFont.render("This planet is the only one suited for human habitants.", 1, white)
dearth1 = myFont.render("However, Earth is dying because of global warming.", 1, white)
dearth2 = myFont.render("It is important to understand space exploration", 1, white)
dearth3 = myFont.render("(e.g. finding new habitable planets for humans to live on)", 1, white)
dearth4 = myFont.render("but what comes first is exploring new ways to protect Earth", 1, white)

restart = myFont.render("Restart? (Press R)", 1, white)
done = myFont.render("Quit? (Press Q)", 1, white)
space = myFont.render("Press SPACEBAR to continue", 1, white)
wrong = 0
strikes = myFont.render(str(wrong) + " X", 1, white)
right = 0

character_x = -500
character_y = 100

while gameFinished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameFinished = True

    keys = pygame.key.get_pressed()

    if keys[ord('q')]:
        gameFinished = True

    if keys[ord('r')]:
        beginning = True
        tutorial = False
        loading = False
        success = False
        fail = False
        qmercury = False
        qvenus = False
        qearth = False
        qmars = False
        qjupiter = False
        qsaturn = False
        quranus = False
        qneptune = False
        wrong = 0
        strikes = myFont.render(str(wrong) + " X", 1, white)
        right = 0

    mousecor = pygame.mouse.get_pos()
    mouseXcor = mousecor[0]
    mouseYcor = mousecor[1]

    if beginning == True:
        screen.blit(background, (0, 0))
        screen.blit(title, [390, 200])
        screen.blit(start, [200, 400])
        screen.blit(learn, [750, 400])
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and 200 < mouseXcor < 265 and 400 < mouseYcor < 430:
            loading = True
            beginning = False
        if event.type == pygame.MOUSEBUTTONDOWN and 750 < mouseXcor < 860 and 400 < mouseYcor < 430:
            tutorial = True
            beginning = False

    if tutorial == True:
        screen.blit(background, (0, 0))
        label = myFont.render("Tutorial", 1, white)
        screen.blit(label, [460, 50])
        #pygame.display.update()
        welcome = myFont.render("Help the astronaut find their way back home!", 1, white)
        screen.blit(welcome, [240, 150])
        explanation = myFont.render("You can only get 3 questions wrong before you restart", 1, white)
        screen.blit(explanation, [190, 250])
        final = myFont.render("The final challenge is to answer all of Earth's questions right to get back home", 1, white)
        screen.blit(final, [30, 350])
        intro = myFont.render("To select anything, press the number above your choice", 1, white)
        screen.blit(intro, [160, 450])
        exit = myFont.render("Press Q at anytime to quit and R to restart", 1, white)
        screen.blit(exit, [250, 550])
        end = myFont.render("Most importantly, have fun! :)", 1, white)
        screen.blit(end, [320, 650])
        pygame.display.update()

    if loading == True:
        screen.blit(background, (0, 0))
        screen.blit(strikes, [900, 50])
        choice = myFont.render("Choose a planet", 1, white)
        screen.blit(choice, [400, 70])

        screen.blit(mercury, (140, 250))
        me = myFont.render("Mercury", 1, white)
        screen.blit(me, [150, 370])
        nme = myFont.render("1", 1, white)
        screen.blit(nme, [200, 200])

        screen.blit(venus, (340, 250))
        ve = myFont.render("Venus", 1, white)
        screen.blit(ve, [365, 370])
        nve = myFont.render("2", 1, white)
        screen.blit(nve, [400, 200])

        screen.blit(mars, (540, 250))
        ma = myFont.render("Mars", 1, white)
        screen.blit(ma, [575, 370])
        nma = myFont.render("3", 1, white)
        screen.blit(nma, [600, 200])

        screen.blit(jupiter, (740, 250))
        ju = myFont.render("Jupiter", 1, white)
        screen.blit(ju, [765, 370])
        nju = myFont.render("4", 1, white)
        screen.blit(nju, [800, 200])

        screen.blit(saturn, (240, 500))
        sa = myFont.render("Saturn", 1, white)
        screen.blit(sa, [265, 620])
        nsa = myFont.render("5", 1, white)
        screen.blit(nsa, [300, 450])

        screen.blit(uranus, (440, 500))
        ur = myFont.render("Uranus", 1, white)
        screen.blit(ur, [460, 620])
        nur = myFont.render("6", 1, white)
        screen.blit(nur, [500, 450])

        screen.blit(neptune, (640, 500))
        ne = myFont.render("Neptune", 1, white)
        screen.blit(ne, [655, 620])
        nne = myFont.render("7", 1, white)
        screen.blit(nne, [700, 450])

        pygame.display.update()

        if keys[pygame.K_1]:
            qmercury = True
            loading = False

        if keys[pygame.K_2]:
            qvenus = True
            loading = False

        if keys[pygame.K_3]:
            qmars = True
            loading = False

        if keys[pygame.K_4]:
            qjupiter = True
            loading = False

        if keys[pygame.K_5]:
            qsaturn = True
            loading = False

        if keys[pygame.K_6]:
            quranus = True
            loading = False

        if keys[pygame.K_7]:
            qneptune = True
            loading = False

    if qmercury == True:
        screen.blit(background, (0, 0))
        screen.blit(bigmercury, (-530, 400))
        screen.blit(astronaut, (430, 300))
        # pygame.draw.rect(screen, white, [50, 50, 600, 400])
        screen.blit(strikes, [900, 50])

        temperature = myFont.render("What is the temperature of Mercury in celcius", 1, white)
        screen.blit(temperature, [100, 100])
        t1 = myFont.render("a) -200 to -600", 1, white)
        screen.blit(t1, [100, 200])
        t2 = myFont.render("b) 430 to -170", 1, white)
        screen.blit(t2, [400, 200])
        t3 = myFont.render("c) -50 to 120", 1, white)
        screen.blit(t3, [700, 200])
        pygame.display.update()

        if keys[ord('a')]:
            screen.blit(background, (0, 0))
            screen.blit(bigmercury, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dmercury, [40, 200])
            screen.blit(dmercury1, [70, 250])
            screen.blit(dmercury2, [250, 300])
            pygame.display.update()
            qmercury = False

        if keys[ord('b')]:
            right += 1
            screen.blit(background, (0, 0))
            screen.blit(bigmercury, (-530, 400))
            screen.blit(astronaut, (430, 300))
            screen.blit(strikes, [900, 50])
            screen.blit(correct, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dmercury, [40, 200])
            screen.blit(dmercury1, [70, 250])
            screen.blit(dmercury2, [250, 300])
            pygame.display.update()
            qmercury = False

        if keys[ord('c')]:
            screen.blit(background, (0, 0))
            screen.blit(bigmercury, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dmercury, [40, 200])
            screen.blit(dmercury1, [70, 250])
            screen.blit(dmercury2, [250, 300])
            pygame.display.update()
            qmercury = False
###############################################################################################
    if qvenus == True:
        screen.blit(background, (0, 0))
        screen.blit(bigvenus, (-530, 400))
        screen.blit(astronaut, (430, 300))
        # pygame.draw.rect(screen, white, [50, 50, 600, 400])
        screen.blit(strikes, [900, 50])

        radius = myFont.render("What is the radius of Venus in kilometers?", 1, white)
        screen.blit(radius, [100, 100])
        r1 = myFont.render("a) 6051.8 km", 1, white)
        screen.blit(r1, [100, 200])
        r2 = myFont.render("b) 7012.9 km", 1, white)
        screen.blit(r2, [400, 200])
        r3 = myFont.render("c) 212.2 km", 1, white)
        screen.blit(r3, [700, 200])
        pygame.display.update()

        if keys[ord('a')]:
            right += 1
            screen.blit(background, (0, 0))
            screen.blit(bigvenus, (-530, 400))
            screen.blit(astronaut, (430, 300))
            screen.blit(strikes, [900, 50])
            screen.blit(correct, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dvenus, [240, 200])
            screen.blit(dvenus1, [10, 250])
            screen.blit(dvenus2, [30, 300])
            pygame.display.update()
            qvenus = False

        if keys[ord('b')]:
            screen.blit(background, (0, 0))
            screen.blit(bigvenus, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dvenus, [240, 200])
            screen.blit(dvenus1, [10, 250])
            screen.blit(dvenus2, [30, 300])
            pygame.display.update()
            qvenus = False

        if keys[ord('c')]:
            screen.blit(background, (0, 0))
            screen.blit(bigvenus, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dvenus, [240, 200])
            screen.blit(dvenus1, [10, 250])
            screen.blit(dvenus2, [30, 300])
            pygame.display.update()
            qvenus = False
####################################################################

    if qmars == True:
        screen.blit(background, (0, 0))
        screen.blit(bigmars, (-530, 400))
        screen.blit(astronaut, (430, 300))
        # pygame.draw.rect(screen, white, [50, 50, 600, 400])
        screen.blit(strikes, [900, 50])

        years = myFont.render("How long is year on Mars (in Earth days)?", 1, white)
        screen.blit(years, [100, 100])
        y1 = myFont.render("a) 687 days", 1, white)
        screen.blit(y1, [100, 200])
        y2 = myFont.render("b) 320 days", 1, white)
        screen.blit(y2, [400, 200])
        y3 = myFont.render("c) 4 years", 1, white)
        screen.blit(y3, [700, 200])
        pygame.display.update()

        if keys[ord('a')]:
            right += 1
            screen.blit(background, (0, 0))
            screen.blit(bigmars, (-530, 400))
            screen.blit(astronaut, (430, 300))
            screen.blit(strikes, [900, 50])
            screen.blit(correct, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dmars, [230, 200])
            screen.blit(dmars1, [250, 250])
            screen.blit(dmars2, [200, 300])
            screen.blit(dmars3, [60, 350])
            pygame.display.update()
            qmars = False

        if keys[ord('b')]:
            screen.blit(background, (0, 0))
            screen.blit(bigmars, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dmars, [230, 200])
            screen.blit(dmars1, [250, 250])
            screen.blit(dmars2, [200, 300])
            screen.blit(dmars3, [60, 350])
            pygame.display.update()
            qmars = False

        if keys[ord('c')]:
            screen.blit(background, (0, 0))
            screen.blit(bigmars, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dmars, [230, 200])
            screen.blit(dmars1, [250, 250])
            screen.blit(dmars2, [200, 300])
            screen.blit(dmars3, [60, 350])
            pygame.display.update()
            qmars = False
###################################################################
    if qjupiter == True:
        screen.blit(background, (0, 0))
        screen.blit(bigjupiter, (-530, 400))
        screen.blit(astronaut, (430, 300))
        # pygame.draw.rect(screen, white, [50, 50, 600, 400])
        screen.blit(strikes, [900, 50])

        radius = myFont.render("What is the radius of Jupiter (in kilometers)?", 1, white)
        screen.blit(radius, [100, 100])
        r1 = myFont.render("a) 80, 741 km, ", 1, white)
        screen.blit(r1, [100, 200])
        r2 = myFont.render("b) 57,638 km", 1, white)
        screen.blit(r2, [400, 200])
        r3 = myFont.render("c) 69,811 km", 1, white)
        screen.blit(r3, [700, 200])
        pygame.display.update()

        if keys[ord('a')]:
            screen.blit(background, (0, 0))
            screen.blit(bigjupiter, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(djupiter, [200, 200])
            screen.blit(djupiter1, [25, 250])
            pygame.display.update()
            qjupiter = False

        if keys[ord('b')]:
            screen.blit(background, (0, 0))
            screen.blit(bigjupiter, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(djupiter, [200, 200])
            screen.blit(djupiter1, [25, 250])
            pygame.display.update()
            qjupiter = False

        if keys[ord('c')]:
            right += 1
            screen.blit(background, (0, 0))
            screen.blit(bigjupiter, (-530, 400))
            screen.blit(astronaut, (430, 300))
            screen.blit(strikes, [900, 50])
            screen.blit(correct, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(djupiter, [200, 200])
            screen.blit(djupiter1, [25, 250])
            pygame.display.update()
            qjupiter = False

############################################################
    if qsaturn == True:
        screen.blit(background, (0, 0))
        screen.blit(bigsaturn, (-530, 400))
        screen.blit(astronaut, (430, 300))
        # pygame.draw.rect(screen, white, [50, 50, 600, 400])
        screen.blit(strikes, [900, 50])

        temperature = myFont.render("What is the temperature of Saturn in celcius?", 1, white)
        screen.blit(temperature, [100, 100])
        t1 = myFont.render("a) 246°C", 1, white)
        screen.blit(t1, [100, 200])
        t2 = myFont.render("b) -139°C", 1, white)
        screen.blit(t2, [400, 200])
        t3 = myFont.render("c) -48°C", 1, white)
        screen.blit(t3, [700, 200])
        pygame.display.update()

        if keys[ord('a')]:
            screen.blit(background, (0, 0))
            screen.blit(bigsaturn, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dsaturn, [15, 200])
            pygame.display.update()
            qsaturn = False

        if keys[ord('b')]:
            right += 1
            screen.blit(background, (0, 0))
            screen.blit(bigsaturn, (-530, 400))
            screen.blit(astronaut, (430, 300))
            screen.blit(strikes, [900, 50])
            screen.blit(correct, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dsaturn, [15, 200])
            pygame.display.update()
            qsaturn = False

        if keys[ord('c')]:
            screen.blit(background, (0, 0))
            screen.blit(bigsaturn, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dsaturn, [15, 200])
            pygame.display.update()
            qsaturn = False

###########################################
    if quranus == True:
        screen.blit(background, (0, 0))
        screen.blit(biguranus, (-530, 400))
        screen.blit(astronaut, (430, 300))
        #pygame.draw.rect(screen, white, [50, 50, 600, 400])
        screen.blit(strikes, [900, 50])

        years = myFont.render("How long is a year on Uranus (in Earth days)?", 1, white)
        screen.blit(years, [100, 100])
        y1 = myFont.render("a) 68 years", 1, white)
        screen.blit(y1, [100, 200])
        y2 = myFont.render("b) 84 years", 1, white)
        screen.blit(y2, [400, 200])
        y3 = myFont.render("c) 72 years", 1, white)
        screen.blit(y3, [700, 200])
        pygame.display.update()

        if keys[ord('a')]:
            screen.blit(background, (0, 0))
            screen.blit(biguranus, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(duranus, [200, 200])
            screen.blit(duranus1, [35, 250])
            pygame.display.update()
            quranus = False

        if keys[ord('b')]:
            right += 1
            screen.blit(background, (0, 0))
            screen.blit(biguranus, (-530, 400))
            screen.blit(astronaut, (430, 300))
            screen.blit(strikes, [900, 50])
            screen.blit(correct, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(duranus, [200, 200])
            screen.blit(duranus1, [35, 250])
            pygame.display.update()
            quranus = False

        if keys[ord('c')]:
            screen.blit(background, (0, 0))
            screen.blit(biguranus, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(duranus, [200, 200])
            screen.blit(duranus1, [35, 250])
            pygame.display.update()
            quranus = False
################################################################
    if qneptune == True:
        screen.blit(background, (0, 0))
        screen.blit(bigneptune, (-530, 400))
        screen.blit(astronaut, (430, 300))
        #pygame.draw.rect(screen, white, [50, 50, 600, 400])
        screen.blit(strikes, [900, 50])

        radius = myFont.render("What is the radius of Neptune in kilometers?", 1, white)
        screen.blit(radius, [100, 100])
        r1 = myFont.render("a) 1382.34 km", 1, white)
        screen.blit(r1, [100, 200])
        r2 = myFont.render("b) 3456.78 km", 1, white)
        screen.blit(r2, [400, 200])
        r3 = myFont.render("c) 2439.7 km", 1, white)
        screen.blit(r3, [700, 200])
        pygame.display.update()

        if keys[ord('a')]:
            screen.blit(background, (0, 0))
            screen.blit(bigneptune, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dneptune, [220, 200])
            screen.blit(dneptune1, [230, 250])
            screen.blit(dneptune2, [150, 300])
            pygame.display.update()
            qneptune = False

        if keys[ord('b')]:
            screen.blit(background, (0, 0))
            screen.blit(bigneptune, (-530, 400))
            screen.blit(astronaut, (430, 300))
            wrong += 1
            strikes = myFont.render(str(wrong) + " X", 1, white)
            screen.blit(strikes, [900, 50])
            screen.blit(incorrect, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dneptune, [220, 200])
            screen.blit(dneptune1, [230, 250])
            screen.blit(dneptune2, [150, 300])
            pygame.display.update()
            qneptune = False

        if keys[ord('c')]:
            right += 1
            screen.blit(background, (0, 0))
            screen.blit(bigneptune, (-530, 400))
            screen.blit(astronaut, (430, 300))
            screen.blit(strikes, [900, 50])
            screen.blit(correct, [450, 50])
            screen.blit(space, [310, 100])
            screen.blit(dneptune, [220, 200])
            screen.blit(dneptune1, [230, 250])
            screen.blit(dneptune2, [150, 300])
            pygame.display.update()
            qneptune = False

####################################################################
    if qearth == True:
        screen.blit(background, (0, 0))
        screen.blit(bigearth, (-530, 400))
        screen.blit(astronaut, (430, 300))
        # pygame.draw.rect(screen, white, [50, 50, 600, 400])
        screen.blit(strikes, [900, 50])

        question = myFont.render("How many greenhouse gases are emitted every year on Earth?", 1, white)
        screen.blit(question, [100, 100])
        q1 = myFont.render("a) 1 trillion tonnes", 1, white)
        screen.blit(q1, [100, 200])
        q2 = myFont.render("b) 102 billion tonnes", 1, white)
        screen.blit(q2, [400, 200])
        q3 = myFont.render("c) 50 billion tonnes", 1, white)
        screen.blit(q3, [700, 200])
        pygame.display.update()

        if keys[ord('a')]:
            fail = True
            qearth = False

        if keys[ord('b')]:
            fail = True
            qearth = False

        if keys[ord('c')]:
            success = True
            qearth = False

    if right + wrong == 7:
        loading = False
        while character_x != 300:
            screen.blit(background, (0, 0))
            boss = myFont.render("This is your final question to save the astronaut", 1, white)
            screen.blit(boss, [220, 200])
            screen.blit(earth, [450, 300])
            screen.blit(name, [character_x, character_y])
            character_x += 1
            pygame.display.update()
        right += 1
        qearth = True

    if keys[pygame.K_SPACE]:
        loading = True
        qmercury = False
        qvenus = False
        qearth = False
        qmars = False
        qjupiter = False
        qsaturn = False
        quranus = False
        qneptune = False

    if success == True:
        screen.blit(background, (0, 0))
        screen.blit(bigearth, (-530, 400))
        yay = myFont.render("Congratulations, you saved the astronaut!", 1, white)
        screen.blit(yay, [250, 50])
        screen.blit(astronaut, (430, 300))
        screen.blit(restart, [200, 100])
        screen.blit(done, [600, 100])
        screen.blit(strikes, [900, 50])
        screen.blit(dearth, [170, 200])
        screen.blit(dearth1, [180, 250])
        screen.blit(dearth2, [210, 300])
        screen.blit(dearth3, [150, 350])
        screen.blit(dearth4, [140, 400])
        pygame.display.update()

    if fail == True:
        screen.blit(background, (0, 0))
        screen.blit(bigearth, (-530, 400))
        boo = myFont.render("Mission Failed, better luck next time!", 1, white)
        screen.blit(boo, [300, 200])
        screen.blit(astronaut, (430, 300))
        screen.blit(restart, [200, 300])
        screen.blit(done, [600, 300])
        screen.blit(strikes, [900, 50])
        pygame.display.update()

    if wrong == 3:
        fail = True
        beginning = False
        tutorial = False
        loading = False
        success = False

        qmercury = False
        qvenus = False
        qearth = False
        qmars = False
        qjupiter = False
        qsaturn = False
        quranus = False
        qneptune = False

pygame.quit()
quit()