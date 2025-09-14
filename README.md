# Contextual Text Summarizer

A smart text summarizer that creates short summaries from long conversations and documents using advanced AI models.

## What This Project Does

This project takes long text conversations like chat logs or dialogues and automatically creates short, meaningful summaries. It uses a powerful AI model called Pegasus to understand the context and generate accurate summaries.

## Key Features

- Automatically summarizes long conversations into short summaries
- Uses pre-trained AI model for high quality results
- Complete pipeline from data loading to model evaluation
- Easy to use configuration system
- Detailed logging and monitoring
- Model performance evaluation with metrics

## How It Works

The project follows these main steps:

1. **Data Collection**: Downloads and prepares conversation datasets
2. **Data Processing**: Cleans and formats the text data for training
3. **Model Training**: Fine-tunes the Pegasus model on conversation data
4. **Evaluation**: Tests the model performance using standard metrics
5. **Summary Generation**: Creates summaries for new conversations

## Technologies Used

- Python programming language
- Hugging Face Transformers library
- PyTorch deep learning framework
- Pegasus model for text summarization
- ROUGE metrics for evaluation
- YAML for configuration management

## Project Structure

The project is organized into clear modules:

- **src/Contextual_Summarizer**: Main source code
  - **components**: Core functionality for each pipeline stage
  - **config**: Configuration management
  - **pipeline**: End-to-end workflow orchestration
  - **utils**: Helper functions and utilities
  - **logging**: System logging setup
- **config**: Configuration files
- **research**: Jupyter notebooks for experimentation
- **artifacts**: Generated models and data

## Installation and Setup

1. Clone this repository to your computer
2. Install Python 3.8 or higher
3. Install required packages using: pip install -r requirements.txt
4. Run the main pipeline: python main.py

## Usage Example

The system can process any conversation text and generate summaries. For example:

Input conversation: Long dialogue between two people discussing a project
Output summary: Brief overview of the main discussion points and decisions

## Model Performance

The model is evaluated using ROUGE metrics which measure summary quality:
- ROUGE-1: Measures single word overlap
- ROUGE-2: Measures two-word phrase overlap
- ROUGE-L: Measures longest common sequence

## Real-World Applications

This summarizer can be used for:

- Customer service chat summarization
- Meeting notes generation
- Email thread summaries
- Social media conversation analysis
- Document summarization
- News article summarization

## Business Value

- Saves time by automatically creating summaries
- Improves information processing efficiency
- Helps in quick decision making
- Reduces manual review workload
- Enables better information organization

## Future Enhancements

Potential improvements for this project:
- Web interface for easy use
- Support for multiple languages
- Real-time summarization
- Custom domain adaptation
- Batch processing capabilities
- API for integration with other systems

## Technical Skills Demonstrated

This project showcases:
- Machine Learning and Natural Language Processing
- End-to-end ML pipeline development
- Model fine-tuning and evaluation
- Configuration-driven development
- Modular code architecture
- Logging and monitoring implementation
- Data processing and transformation

## Getting Help

If you encounter any issues:
1. Check the logs folder for error messages
2. Verify all dependencies are installed correctly
3. Ensure configuration files are properly set up
4. Review the research notebooks for examples

## License

This project is available for educational and research purposes.

## Contact

For questions or suggestions about this project, please refer to the repository issues section.