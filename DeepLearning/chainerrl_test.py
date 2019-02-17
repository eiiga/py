import gym

# ほうきの倒立運動
# env = gym.make('CartPole-v0')

# パックマン
#env = gym.make('MsPacman-v0')

# スペースインベーダー
env = gym.make('SpaceInvaders-v0')

env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample())
