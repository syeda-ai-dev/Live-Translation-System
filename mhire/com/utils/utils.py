import os

def get_assets_path():
    """Returns the path to the assets directory."""
    current_dir = os.path.dirname(os.path.abspath(__file__))  # utils directory
    com_dir = os.path.dirname(current_dir)  # com directory
    return os.path.join(com_dir, "assets")