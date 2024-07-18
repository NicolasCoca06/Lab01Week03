**Zero-Shot Prompting**

* **Definition:**  A prompting technique where the model is given a task or question it has never seen before, without any examples or training data specifically for that task. The model relies on its general knowledge and understanding of language to complete the task.
* **Example:**  "Translate the following sentence into Spanish: 'The cat sat on the mat.'"

**Few-Shot Prompting**

* **Definition:**  The model is given a few examples (typically 1-5) of the desired input-output pairs before being asked to complete the task. This provides the model with a context and helps it understand the desired format and style of the output.
* **Example:** 
    * **Input:** "Translate the following sentence into Spanish: 'The dog barked.'" 
    * **Output:** "El perro ladró." 
    * **New Input:** "Translate the following sentence into Spanish: 'The bird flew.'"
    * **Desired Output:** "El pájaro voló."

**Chain-of-Thought (CoT) Prompting**

* **Definition:** A prompting technique that encourages the model to reason step-by-step, outlining its thought process in a sequence of logical steps before arriving at a final answer.
* **Example:** "What is the sum of 12 + 13?
   * First, I need to add the ones place: 2 + 3 = 5.
   * Then, I need to add the tens place: 1 + 1 = 2.
   * Therefore, the sum of 12 + 13 is 25."

**Self-Consistency**

* **Definition:** A technique where multiple prompts are generated for the same task, and the model's responses are compared. The final answer is chosen based on consistency and agreement among the different responses. This helps reduce the chance of the model producing a hallucinated or incorrect answer.
* **Example:**  The model is asked the same question with slight variations in wording. If the model gives consistently similar answers, the response is considered more reliable.

**Generate Knowledge Prompting**

* **Definition:** A prompting approach where the model is asked to generate text that includes factual information or knowledge about a particular topic. This type of prompt aims to extract and present knowledge from the model's training data.
* **Example:** "Write a short paragraph about the history of the internet."

**Prompt Chaining**

* **Definition:** A sequence of prompts are given to the model, where each prompt builds upon the previous one. This allows for more complex and nuanced tasks to be completed, as the model can remember and utilize information from earlier prompts.
* **Example:**
    * Prompt 1: "Who is the current president of the United States?"
    * Prompt 2: "What is the name of the current president's wife?"
    * Prompt 3: "What is the name of the current president's dog?"

**Tree of Thoughts**

* **Definition:**  An extension of Chain-of-Thought prompting, where the model explores multiple possible reasoning paths. The model creates a tree-like structure of different thought processes, allowing it to consider various options and make more robust decisions.
* **Example:** A task requiring a multi-step solution, where the model branches out to explore different approaches and their potential outcomes.

**Retrieval Augmented Generation (RAG)**

* **Definition:**  A technique that combines retrieval of relevant information from external knowledge bases with language model generation. This allows the model to access a larger pool of information and produce more accurate and informative responses.
* **Example:**  A question about a specific historical event, where the model retrieves relevant information from a database of historical documents before generating a response.

**Directional Stimulus Prompting**

* **Definition:**  This approach utilizes prompts that provide specific instructions and guide the model towards a particular desired outcome or style.
* **Example:**  "Write a poem in the style of Shakespeare, using iambic pentameter."

**ReAct Prompting**

* **Definition:**  A framework that combines Reasoning, Acting, and Thinking. The model interacts with its environment by taking actions, observing the results, and using this information to reason and plan its next steps.
* **Example:**  A task involving a virtual world or game, where the model can interact with objects, receive feedback, and make decisions based on its understanding of the environment.

**Multimodal CoT Prompting**

* **Definition:**  An extension of Chain-of-Thought prompting that involves combining text with other modalities, such as images or videos. This allows the model to reason and generate responses based on a more comprehensive understanding of the input.
* **Example:**  A task involving a photo and a description, where the model needs to provide a detailed caption that integrates both visual and textual information.

**Key Points:**

* **Prompt Engineering:** These techniques are all part of the field of prompt engineering, which focuses on designing effective prompts that can elicit desired outputs from language models.
* **Evolution of Prompting:**  As language models become more advanced, prompting techniques are constantly evolving to push the boundaries of their capabilities.
* **Task Specificity:** The best prompting technique for a particular task will depend on the specific needs and characteristics of the task.