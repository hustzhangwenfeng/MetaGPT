from ..utils.const import MAZE_ASSET_PATH
from ..maze import Maze

def test_maze_init():
    maze = Maze(maze_asset_path=MAZE_ASSET_PATH)
    assert maze.maze_height == 100
    assert maze.maze_width == 140



