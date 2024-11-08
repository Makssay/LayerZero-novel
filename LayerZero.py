import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_image_base = pygame.image.load('background.jpg')
background_image_first_3_roles = pygame.image.load('background2.jpg')
background_image_AddInformation = pygame.image.load('background3.jpg')
background_image_intern = pygame.image.load('background4.jpg')
background_image_hero = pygame.image.load('background5.jpg')
background_image_OG = pygame.image.load('background6.jpg')
background_image_legend = pygame.image.load('background7.jpg')
background_image_GOD = pygame.image.load('background8.jpg')
background_image_Stargate = pygame.image.load('background9.jpg')
background_image_LZ = pygame.image.load('background10.jpg')
background_image_ULN= pygame.image.load('background11.jpg')
background_image_Security = pygame.image.load('background12.jpg')
background_image_ZRO = pygame.image.load('background13.jpg')
background_image_dev = pygame.image.load('background14.jpg')

pygame.display.set_caption("LayerZero")
persona = pygame.image.load('character.png')
persona2 = pygame.image.load('character2.png')
persona3 = pygame.image.load('character3.png')
dialogue = pygame.image.load("dialogue.png")

pygame.mixer.init()
pygame.mixer.music.load('LayerZero.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font("Monocraft.otf", 20)
name = font.render("Bryan", True, WHITE)


ape_names = ["Bryan", "Ape One", "Ape Two"]
current_name_index = 0
choice_rects = []


intro_text = [
    "Welcome to the LayerZero office.",
    "A tour of our project awaits you here!",
    "My name is Bryan Pellegrino.",
    "I am the Co-Founder of LayerZero.",
    "Let's start our tour."
]


main_menu_text = "What do you want to know?"
choices = {
    "What is LayerZero?": ["I'm glad you didn't close the game right after you  moved on to the answer options.",
                           "now I will briefly tell you what LayerZero","LayerZero is a protocol for cross-chain  communication that allows the exchange of data and assets between different blockchains with minimal computational costs.",
                           "It uses repeaters and oracles to ensure security andconfirm transactions",
                           "The LayerZero architecture helps to avoid vulnerabilities of traditional bridges and simplifies integration between different blockchains",
                           "LayerZero works on the omnichain principle, which means that users and developers can interact with any blockchains in a single interface",],
    "Discord Role": [""],
    "What do I need to know?": ["go"],
    "GAME": ["GOOD GAME"],
    "From developer": ["Hi, now I want to speak out a little bit",
                       "The game didn't turn out to be as global as I had   planned",
                       "The decision to post this version of the game was made due to personal deadlines and if I hadn't posted it now, you wouldn't have seen it soon",
                       "in the near future, I plan to make a new version of the storyline game about LayerZero",
                       "if this idea gets a lot of attention",
                       "anyway, I managed to gather all the necessary information so that new members could understand LayerZero",
                       "Thank you for your attention",
                       "subscribe to my Twitter"]
}






what_you_need_to_know_variants = {
    "LayerZero x APE": ["Hello APE",
                        "Hello Bryan",
                        "I want to tell you about our interaction with your  token",
                        "Okay let's go",
                        "LayerZero and ApeCoin interact to ensure cross-chain compatibility, which allows ApeCoin to be used on  different blockchains.",
                        "Understood. And why does ApeCoin need this?",
                        "ApeCoin a token that is used in the BAYC ecosystem. Integration with LayerZero allows ApeCoin owners to freely move the token between different blockchains.This expands its capabilities by making it available to more decentralized applications.",
                        'So I can use ApeCoin on different networks?',
                        'Yes, exactly! Thanks to LayerZero, you can move  ApeCoin between networks, which makes it more flexible and accessible. It also reduces transaction costs   and simplifies interaction with the token.',
                        "That's cool! so I can use ApeCoin more effectively  in the Web3 ecosystem",
                        "Absolutely! ApeCoin is becoming a more versatile    tool that can be used in various networks and       decentralized applications."],

    "Stargate": ["Stargate is a protocol for cross-chain data transfer based on the LayerZero infrastructure. It enables  secure and fast transfers of tokens and data between various blockchains, such as Ethereum, Binance     Smart Chain, and others.",
                 "Stargate uses LayerZero unique technology to ensure secure data transfer between networks. The protocol minimizes the risks of double spending and other    attacks commonly associated with cross-chain protocols.",
                 "Stargate allows users to access liquidity pools     across different networks without needing separate  liquidity for each.This enhances asset accessibility and simplifies cross-chain transactions.",
                 "Stargate offers near-instant confirmation of transactions, reducing wait times associated with moving   funds between networks."],

    "Security": ["Security and decentralization are the key principlesof LayerZero.",
                 "LayerZero offers a high level of security and decentralization, using modern encryption methods to protect data",
                 "Network management is distributed among the participants, which ensures transparency and stability",
                 "This technology allows you to build decentralized   app that can change the future of the Internet."],

    "Ultra Light Node (ULN)": ["Introducing Ultra Light Node (ULN) by LayerZero",
                               "ULN is a revolution in the field of network technologies. Developed by LayerZero, ULN makes cross-chain transactions instant and secure, while not requiring a full-fledged node.",
                               "How does ULN work?",
                               "ULN uses a lightweight client to work with multiple blockchains, which allows efficient processing of   cross-chain transactions. It collects evidence from different blockchains to ensure their security and  integrity.",
                               "ULN has many advantages, including: ",
                               "1)Instant and secure cross-chain transactions",
                               "2)Efficiency and cost-effectiveness compared to full nodes",
                               "3)Compatibility with multiple blockchains",
                               "4)Improved scalability and throughput"],

    "ZRO tocen": ["The ZERO token is used to participate in protocol management",
                  "token was officially launched in June 2024 with a maximum volume of 1 billion tokens",
                  "In addition, ZRO serves as an incentive for the growth of applications in the LayerZero ecosystem"]
}



discord_role_variants = {
    "The first 3 roles to choose from": ["Community Layer should be chosen by participants who love communication",
                                         "Builder Layer if you are far from blockchain develo-pment or you are just a novice developer, as the au-thor of this program, it does not matter, even this program is suitable for this role",
                                         "Content Layer: you have to create content (videos or Twitter posts), educational or entertaining, it's  not so important, the main thing is that it would be about LayerZero",
                                         "In order to get these roles, you just need to go to the page in our discord that you see behind my back and select the roles by clicking on the reactions under the message"],


    "Intern Role": ["This is the first role you will have to work for", "This role will give you the opportunity to chat in  private chats", "To get this role, you need to be active in the chat and make content on twitter about LayerZero", "More than 450 participants who have this role"],
    "Hero Role": ["Everything is about the same as for interns, but a  level higher. To get this role, you will have to try even harder.", "It's really not easy to get this role, at the moment there are only ~ 15 participants in this role"],
    "OG Role": ["You are very cool if you are on the way to getting  this role (unlike the developer of this game)", "To get this position, you need to be an event organ-izer (or be their co-founder), for example, a Quiz", "You also need to help participants in the chat and make content on twitter"],
    "Legend Role": ["Congratulations, you are close to the elite of the  LayerZero!", "To become a legend, you need to lead initiatives,   create high-quality content, and have a key role in the development of LayerZero"],
    "God Role": ["That's the end of the road, but only one participant will reach it (or maybe no one will get it)", "Yes, you understood everything correctly, only one  participant can get this role", "There are no clear criteria for this role. Your ded-ication to the Layer Zero community will decide if  you can get this role"],
    "Add.Information": ["you do not need to ask the moderators about when you will be assigned to the role. No one likes that.", "LayerZero values its community and maybe there will be a reward for your dedication to the community", "For a potential rebirth, you should join the guild  and get your first `Zero Layer` role"],

}


current_scene = "intro"
current_story = None
current_slide = 0
intro_slide = 0
selected_variant = None
use_new_background = False
use_background_first_3_roles = False
use_background_intern_role = False
use_background_hero_role = False
use_background_OG_role = False
use_background_legend_role = False
use_background_GOD_role = False
use_background_image_Stargate = False
use_background_image_LZ = False
use_background_image_ULN = False
use_background_image_Security = False
use_background_image_ZRO = False
use_background_image_dev = False



def draw_intro():
    screen.blit(background_image_base, (0, 0))
    screen.blit(persona, (-10, 400))
    screen.blit(dialogue, (10, 600))
    screen.blit(name, (30, 640))
    if intro_slide < len(intro_text):
        text_surface = font.render(intro_text[intro_slide], True, WHITE)
        screen.blit(text_surface, (30, 680))

    else:
        draw_main_menu()

    pygame.display.flip()




def draw_main_menu():
    screen.blit(background_image_base, (0, 0))
    screen.blit(persona, (-10, 400))
    screen.blit(dialogue, (10, 600))
    text_surface = font.render(main_menu_text, True, WHITE)
    screen.blit(text_surface, (30, 680))
    screen.blit(name, (30, 640))

    global choice_rects
    choice_rects = []

    y_offset = 150
    for choice in choices:
        choice_rect = draw_choice(choice, 50, y_offset)
        choice_rects.append((choice, choice_rect))
        y_offset += 50

    pygame.display.flip()



def draw_choice(text, x, y):
    choice_surface = font.render(text, True, WHITE)
    choice_rect = choice_surface.get_rect(topleft=(x, y))

    # Рисуем черный прямоугольник на заднем фоне текста
    pygame.draw.rect(screen, BLACK,
                     (choice_rect.x - 10, choice_rect.y - 5, choice_rect.width + 20, choice_rect.height + 10))

    # Рисуем текст поверх черного фона
    screen.blit(choice_surface, (x, y))

    return choice_rect  # Возвращаем прямоугольник, если нужно использовать для кликов


def reset_background_flags():
    global use_new_background, use_background_first_3_roles, use_background_intern_role , use_background_image_Stargate, use_background_image_LZ, use_background_image_ZRO
    global use_background_hero_role, use_background_OG_role, use_background_legend_role, use_background_GOD_role, use_background_image_ULN, use_background_image_Security, use_background_image_dev

    use_new_background = False
    use_background_first_3_roles = False
    use_background_intern_role = False
    use_background_hero_role = False
    use_background_OG_role = False
    use_background_legend_role = False
    use_background_GOD_role = False
    use_background_image_Stargate = False
    use_background_image_LZ = False
    use_background_image_ULN = False
    use_background_image_Security = False
    use_background_image_ZRO = False
    use_background_image_dev = False

def draw_story(slides):
    global use_new_background, use_background_first_3_roles, use_background_intern_role, use_background_image_Stargate, use_background_image_ULN, use_background_image_ZRO
    global use_background_hero_role, use_background_OG_role, use_background_legend_role, use_background_GOD_role, use_background_image_LZ, use_background_image_Security, use_background_image_dev
    global name, persona

    # Определяем, какой фон использовать
    if use_new_background:
        screen.blit(background_image_AddInformation, (0, 0))
    elif use_background_first_3_roles:
        screen.blit(background_image_first_3_roles, (0, 0))
    elif use_background_intern_role:
        screen.blit(background_image_intern, (0, 0))
    elif use_background_hero_role:
        screen.blit(background_image_hero, (0, 0))
    elif use_background_OG_role:
        screen.blit(background_image_OG, (0, 0))
    elif use_background_legend_role:
        screen.blit(background_image_legend, (0, 0))
    elif use_background_GOD_role:
        screen.blit(background_image_GOD, (0, 0))
    elif use_background_image_Stargate:
        screen.blit(background_image_Stargate, (0,0))
    elif use_background_image_LZ:
        screen.blit(background_image_LZ, (0,0))
    elif use_background_image_ULN:
        screen.blit(background_image_ULN,(0,0))
    elif use_background_image_Security:
        screen.blit(background_image_Security,(0,0))
    elif use_background_image_ZRO:
        screen.blit(background_image_ZRO,(0,0))
    elif use_background_image_dev:
        screen.blit(background_image_dev,(0,0))
    else:
        screen.blit(background_image_base, (0, 0))

    # Установка персонажа и имени в зависимости от сцены
    if current_story == choices["From developer"]:
        screen.blit(persona3, (-10, 400))
        name = font.render("MaksSay", True, WHITE)
    elif selected_variant == "LayerZero x APE":
        screen.blit(persona, (-10, 400))
        screen.blit(persona2, (450, 400))

        if current_slide % 2 == 0:
            name = font.render("Bryan", True, WHITE)
        else:
            name = font.render("APE", True, WHITE)
    else:
        screen.blit(persona, (-10, 400))
        name = font.render("Bryan", True, WHITE)

    screen.blit(dialogue, (10, 600))
    screen.blit(name, (30, 640))

    # Отрисовка вариантов с фоном для discord_role_variants и what_you_need_to_know_variants
    if current_story == choices["Discord Role"] and current_slide == 0:
        y_offset = 150
        for variant in discord_role_variants:
            draw_choice(variant, 50, y_offset)
            y_offset += 50

    elif current_story == choices["What do I need to know?"] and current_slide == 0:
        y_offset = 150
        for variant in what_you_need_to_know_variants:
            draw_choice(variant, 50, y_offset)
            y_offset += 50
    else:
        if current_slide < len(slides):
            text = slides[current_slide]
            lines = []
            start = 0
            while start < len(text):
                end = start + 52
                if end >= len(text):
                    end = len(text)
                line = text[start:end]
                lines.append(line)
                start = end

            y_offset = 680
            for line in lines:
                text_surface = font.render(line, True, WHITE)
                screen.blit(text_surface, (30, y_offset))
                y_offset += text_surface.get_height()
        else:
            text_surface = font.render("", True, BLACK)
            screen.blit(text_surface, (50, 50))

    pygame.display.flip()


def play_arcanoid():

    paddle_width, paddle_height = 100, 10
    ball_radius = 10
    block_width, block_height = 75, 20
    blocks = []
    block_rows = 15
    block_cols = 10

    # Загрузка изображений
    block_image = pygame.image.load("burger.png")
    block_image = pygame.transform.scale(block_image, (block_width, block_height))

    ball_image = pygame.image.load("ball.png")
    ball_image = pygame.transform.scale(ball_image, (ball_radius * 2, ball_radius * 2))

    for row in range(block_rows):
        for col in range(block_cols):

            blocks.append(
                pygame.Rect(col * (block_width + 5) + 3, row * (block_height + 5) + 50, block_width, block_height))

    paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 50, paddle_width, paddle_height)
    ball = pygame.Rect(WIDTH // 2 - ball_radius, HEIGHT - 60, ball_radius * 2, ball_radius * 2)
    ball_speed = [4, -4]

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= 5
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += 5

        ball.x += ball_speed[0]
        ball.y += ball_speed[1]


        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]
        if ball.bottom >= HEIGHT:

            return False


        if ball.colliderect(paddle):
            ball_speed[1] = -ball_speed[1]


        for block in blocks[:]:
            if ball.colliderect(block):
                ball_speed[1] = -ball_speed[1]
                blocks.remove(block)


        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle)


        screen.blit(ball_image, (ball.x, ball.y))


        for block in blocks:
            screen.blit(block_image, (block.x, block.y))

        pygame.display.flip()
        clock.tick(60)


    return True


def main():
    global current_scene, current_story, current_slide, intro_slide, selected_variant
    global use_new_background, use_background_first_3_roles, use_background_intern_role, use_background_image_LZ, use_background_image_ULN, use_background_image_ZRO, use_background_image_dev
    global use_background_hero_role, use_background_OG_role, use_background_legend_role, use_background_GOD_role, use_background_image_Stargate, use_background_image_Security

    while True:


        if current_scene == "intro":
            draw_intro()
        elif current_scene == "main_menu":
            draw_main_menu()
        elif current_scene == "story":
            draw_story(current_story)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if current_scene == "intro":
                    intro_slide += 1
                    if intro_slide >= len(intro_text):
                        current_scene = "main_menu"
                elif current_scene == "main_menu":

                    reset_background_flags()
                    selected_variant = None


                    for choice, choice_rect in choice_rects:
                        if choice_rect.collidepoint(mouse_pos):
                            if choice == "GAME":
                                game_completed = play_arcanoid()
                                if game_completed:
                                    current_scene = "main_menu"
                                else:
                                    current_scene = "main_menu"

                            else:
                                current_story = choices[choice]
                                current_slide = 0
                                current_scene = "story"
                            break

                elif current_scene == "story":
                    if current_story == choices["Discord Role"] and current_slide == 0:
                        y_offset = 150
                        for variant in discord_role_variants:
                            variant_rect = pygame.Rect(50, y_offset, 200, 40)
                            if variant_rect.collidepoint(mouse_pos):
                                selected_variant = variant
                                current_story = discord_role_variants[variant]
                                current_slide = 0


                                reset_background_flags()

                                if variant == "The first 3 roles to choose from":
                                    use_background_first_3_roles = True
                                elif variant == "Intern Role":
                                    use_background_intern_role = True
                                elif variant == "Hero Role":
                                    use_background_hero_role = True
                                elif variant == "OG Role":
                                    use_background_OG_role = True
                                elif variant == "Legend Role":
                                    use_background_legend_role = True
                                elif variant == "God Role":
                                    use_background_GOD_role = True
                                elif variant == "Add.Information":
                                    use_new_background = True


                                break
                            y_offset += 50

                    if current_story == choices["What do I need to know?"] and current_slide == 0:
                        y_offset = 150
                        for variant in what_you_need_to_know_variants:
                            variant_rect = pygame.Rect(50, y_offset, 200, 40)
                            if variant_rect.collidepoint(mouse_pos):
                                selected_variant = variant
                                current_story = what_you_need_to_know_variants[variant]
                                current_slide = 0
                                reset_background_flags()
                                if variant == "Stargate":
                                    use_background_image_Stargate = True
                                elif variant == "Ultra Light Node (ULN)":
                                    use_background_image_ULN = True
                                elif variant == "Security":
                                    use_background_image_Security = True
                                elif variant == "ZRO tocen":
                                    use_background_image_ZRO = True
                                break
                            y_offset += 50

                    if current_story == choices["What is LayerZero?"] and current_slide == 0:
                        use_background_image_LZ = True

                        current_slide += 1
                    if current_story == choices["From developer"] and current_slide == 0:
                        use_background_image_dev = True


                        current_slide += 1
                    else:
                        current_slide += 1
                        if current_slide >= len(current_story):
                            current_scene = "main_menu"

                            reset_background_flags()




        pygame.display.flip()





if __name__ == "__main__":
    main()