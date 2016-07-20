from src import Timeline
from src.webapp_flask import _entries as entries
if __name__ == '__main__':
    entries.append(Timeline("20150722", "Neophyte",
                            "It all started on 22nd of July, when I was assigned a problem which was to group sentences into clusters based on their tense"))
    entries.append(Timeline("20150808", "Sentiment Analysis",
                            "The Algorithm is based on Bayes Probabilistic model. Sentiment words are detected by using pos-comments and neg-comments text files. The probability of each word is based on the appearance of the word in a sentence which results in the sentence being either positive or negative. The pos/neg files are constructed based on IMDB's Sentimental reviews and twitter's sentiments"))
    entries.append(Timeline("20150905", "Math ML Course",
                            "A course that lasted 6 months inclusive of weekend exams, enabled us to have a better understanding of Mathematical concepts in Machine Learning Techniques"));
    entries.append(Timeline("20150925", "Neural Networks",
                            "Neural networks are models of biological neural structures. The starting point for most neural networks is a model neuron. It consists of multiple inputs and a single output. Each input is modified by a weight, which multiplies with the input value. The neuron will combine these weighted inputs and, with reference to a threshold value and activation function, use these to determine its output"))
    entries.append(Timeline("20151009", "Restricted Boltzmann Machine (RBM)",
                            "In layman's language, it is a generative stochastic neural network that can learn the probability distribution over a set of inputs. It is composed of three layers: Visible Layer, Hidden Layer and Bias Layer"))
    entries.append(Timeline("20151015", "Image Utilities",
                            "My contribution to the RZT Utilities is a set of Image processing methods such as encoding and decoding, Greyscale to Monochrome conversions and others. The utils will be used for image data extraction in the near future"))
    entries.append(Timeline("20151018", "Natural Language Processing(NLP)",
                            "Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of human–computer interaction. I worked on parsing Natural language commands to Machine level commands"))
    entries.append(Timeline("20151025", "Sense Algorithm (Summary)",
                            "The essence of the sentence lies in the context. Usually the context is described by adjectives or adverbs. The usage and frequency of these words predict the importance of a sentence. Hence TF-IDF algorithm is used to calculate the frequency of these words, later Probability Theory is applied to find the probability of the sentence being important"))
    entries.append(Timeline("20151029", "AI Game",
                            "I was assigned to understand and implement Q-Learning Technique. What better way to do it than building a game which incorporates Q- Learning! So a Tic Tac Toe game was built, it has the ability to learn from human moves and decide between draws and wins"))
    entries.append(Timeline("20151102", "Parser Utilities",
                            "This is my contribution to the RZT Utilities. Parser utilities can be used to extract and store data from various filetypes such as CSV,TSV,XLS,XLSX file formats. We will use these utilities in data-preparation stage of BigBrain"))
    entries.append(Timeline("20151110", "Numenta Reserch",
                            "Numenta is a Machine Intelligence Technology used to solve complex problems, and the core is modeled upon the Human Brain's Interaction, Think, Apply functionalities"))
    entries.append(Timeline("20151122", "NER Tagging",
                            "Named Entities, one of the most important features in email - Information Extraction is a tough one. I wrote wrappers on top of Stanford NER which increased its accuracy by 25%"))
    entries.append(Timeline("20151202", "IManagement",
                            "Our contribution towards solving problems in Razorthink Company. IManagement is a smart webapp aimed to manage Razorthink's inventory. Shreesha and I are proud to say that we utilized 4 Saturdays to build the application. Shreesha worked on the backend while I worked on the frontend. The application uses latest technologies like sprint-boot, hibernate, angular and materialize framework"))
    entries.append(Timeline("20151222", "Word2Vec",
                            "The hottest topic in ML and AI. Word2vec is a group of related models that are used to produce so-called word embeddings. These models are shallow, two-layer neural networks that are trained to reconstruct linguistic contexts of words: the network is shown a word, and must guess which words occurred in adjacent positions in an input text"))
    entries.append(Timeline("20151230", "Neo4J",
                            "An opensource graph based database. The idea was to capture the various relations between a person and entities such as another person, organization or location. The algorithms will be used for Information Extraction from electronic mails"))
    entries.append(Timeline("20160102", "Feature Discovery and Pattern Clustering",
                            "An amazing research and development in the field of AI led by Nandu and Shams. We wrote algorithms based on ML top tools such as Word2Vec, Cosine Similarity, Eucledian distance, NER, POS Prediction and others"))
    entries.append(Timeline("20160119", "BigBrain",
                            "The future! Currently, I am working with the BigBrain team. We incorporate today's top notch tech to build a product for Big Data Analysis"))
    entries.append(Timeline("20160206", "Proud Moment - Mysore Recruitment Drive",
                            "6 Months was all that it took for me to move from interviewee to interviewer. My college, my lecturers were proud when they saw their student visit the college for a recruitment drive. I am thankful to RZT for this change in such a short span"))
    entries.append(Timeline("20160228", "Here I am",
                            "RZT has give me a <u><i style='font-style: italic;'>mentor</i></u> like <b style='font-weight: bolder;'>Shams</b>, <u><i style='font-style: italic;'>seniors</i></u> like <b style='font-weight: bolder;'>Amith, Subbu, Abhishek, Shubhadeep, Sajesh, Keerthi</b> and <b style='font-weight: bolder;'>Shreesha</b>, <u><i style='font-style: italic;'>friends</i></u> like <b style='font-weight: bolder;'>Shreesha, Sumith, Swamy, Himaprasoon</b>,  with <u><i style='font-style: italic;'>visionaries</i></u> such as <b style='font-weight: bolder;'>Nandu, Vinay</b> and <b style='font-weight: bolder;'> Jack</b>. Truly I am blessed! <br/><br/>Thank you RZT for an exciting Journey. I can feel the future to be even more compelling and zestful :)"))
