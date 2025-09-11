import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from src.Contextual_Summarizer.logging import logger
from typing import Any
from pathlib import Path
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file
    
    Raises:
        e: BoxValueError if the yaml file is empty
        e: Exception if any other exception occurs

    Returns:
        ConfigBox: ConfigBox object containing the yaml file contents
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"yaml file: {path_to_yaml} is empty: {e}")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True): 
    """Creates a list of directories

    Args:
        path_to_directories (list): List of paths to directories
        verbose (bool, optional): Whether to log the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


    
    