import neat
import pyglet
import map as m
import score as s

window = pyglet.window.Window(1280, 720)
gen = 0
score = s.Score()


def main(genomes, config):
    global window, gen, score
    gen += 1
    score.reset()
    map = m.Map(window)
    map.createAsteroids(1)
    nets = []

    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0
        map.createRockets(1)

    while True:
        pyglet.clock.tick()
        window.dispatch_events()
        window.clear()
        score.label().draw()

        pyglet.text.Label('Gen: {0}'.format(str(gen)),
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width - 200,
                          y=10).draw()

        map.draw()

        for i, rocket in enumerate(map.rockets):
            output = nets[i].activate([rocket.sprite.y] + rocket.radarData)
            if output[0] > 0.5:
                rocket.right()
            if output[1] > 0.5:
                rocket.left()

        for i, rocket in enumerate(map.rockets):
            if rocket.alive == True:
                genomes[i][1].fitness += 0.1

        score.add(1)
        if map.gameOver():
            break

        window.flip()

# @window.event
# def on_key_press(symbol, modifiers):
#     if symbol == key.A:
#         rockets.rockets[0].direction = key.LEFT
#     elif symbol == key.D:
#         rockets.rockets[0].direction = key.RIGHT
#     rockets.rockets[0].steering = True
#
# @window.event
# def on_key_release(symbol, modifier):
#     rockets.rockets[0].steering = False

if __name__ == "__main__":
    # Set configuration file
    config_path = "./config-feedforward.txt"
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Create core evolution algorithm class
    p = neat.Population(config)

    # Add reporter for fancy statistical result
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run NEAT
    p.run(main, 9999)