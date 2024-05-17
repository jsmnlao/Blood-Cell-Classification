# Introduction
Our Blood Cell Classification neural network model focuses on analyzing a blood cell dataset that contains images of four different white blood cells with corresponding labels. The objective of our project is to use CNN (Convolutional Neural Networks) to classify these images as accurately as possible. Our project is significant because blood cell classification is crucial in identifying blood-related diseases, which can help medical professionals conduct diagnoses and research more efficiently. Overall, the usage of neural networks to correctly identify blood cell types can assist in diagnosing illnesses related to white blood cells and improve patient outcomes. Classifying these blood cell types is an important task in the medical field because it allows for an accurate diagnosis of blood-based diseases, such as leukemia and anemia. 

# Kaggle Dataset
Our chosen dataset from Kaggle “Blood Cell Images”, provides an extensive collection of blood cell images with their corresponding labels in which we can use to train and evaluate our model. Our Kaggle dataset contains 12,500 images of blood cells, with roughly 3,000 images per blood cell type. In addition to original images, the dataset also contains augmented images from transformation techniques such as rotation, flips, and cropping. The link to our blood cell dataset can be found here: [Blood Cell Images](https://www.kaggle.com/datasets/paultimothymooney/blood-cells).

# Evaluation Metrics
The evaluation metrics used to evaluate the general performance of our model include accuracy, loss, and F1-score. Accuracy is used to measure the general performance of our model, and because there is no particular dominating class label, this metric is suitable. Loss values indicate that our model’s predictions are close to actual values and help determine accurate predictions. Lastly, the F1-score can help us further improve and minimize our model’s error as it provides a balanced evaluation.

# Results
For the initial training of our custom model, the preset number of epochs was set to 20. The training scores were decently high, at around 83%, but the testing scores were low, at around 65%. The higher training score implies overfitting. Upon graphing the results, it was found that the model stopped improving at around 15 epochs, so this amount was adjusted to help prevent overfitting. This adjustment significantly improved the training and testing scores to 97% and 80% respectively. This demonstrates that our custom model is generally effective at classifying unseen data. However, the higher training accuracy over test accuracy still implies some amount of overfitting and possible opportunities for fine-tuning the model.

Visualizations also indicate our VGG model’s proficiency in learning from the training data, but the testing accuracy at 40% indicates that it does not generalize as well on unseen data. Regarding loss metrics, the training loss decreases to around 0.9, which is not as ideal but reflects the model’s ability to minimize errors throughout training. In contrast, the validation loss shows a sharp increase in loss in the last two epochs, which indicates some overfitting. Lastly, the F1-score for validation and testing are 65% and 32% respectively, which indicates the model’s overall performance and effectiveness at correctly classifying the data. 

Currently, the custom model has better performance than the pre-trained VGG16 model. The custom model is better at generalizing on unseen data and experiences less loss by completion of the training process. Both models have some issues with overfitting, which can be improved with further tuning and experimentation. The training process for the custom model is faster on average, ranging from 10-15 minutes on the GPU provided by Google Colab. The VGG16 model takes slightly longer, at 20 minutes on the same GPU.

# Future Work
Overall, our Blood Type Classification project with CNN determined that our custom model performed better than our pre-trained VGG model, according to the evaluation metric values. Some other key findings include learning about the significance of data preprocessing and hyperparameter tuning to improve our models’ performance. 

For future work, we suggest choosing different pre-trained models, such as ResNet and Inception, over VGG16 to see if they can perform better than our custom model. In addition, we can also try expanding our dataset to include a more diverse range of blood cell images, using ensemble learning methods to combine multiple models, and taking advantage of advanced preprocessing techniques. 
