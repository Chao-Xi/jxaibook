# 1 Introduction to Developing AI Agents

## 2 Understanding Fundamental Concepts of AI Agents


Here's a concise summary of the key points about AI agents from the provided text:

1.  **Definition:** An AI agent is an entity that perceives its environment (physical or digital) through sensors and acts upon that environment using effectors (per ISO definition).


2.  **Core Components:**
    *   **Sensors:** Gather raw data (percepts) from the environment (e.g., cameras, microphones, API calls).
    *   **Control Center:** The "brain" processes percepts, makes decisions, and plans actions (often using an LLM).
    *   **Effectors/Actuators:** Carry out actions to change the environment (e.g., moving an arm, updating a database, generating a report).
    *   **Environment:** The world (physical or digital) the agent operates within.
    *   **User Input:** External input provided (e.g., commands, data) usually by humans or other agents.
    *   **Percepts:** Raw data inputs from sensors.
    *   **Actions:** Changes made in the environment by effectors.


**An agent is anything that can perceive its environment and act upon that environment.**

![Alt Image Text](../images/chap8_1_1.png "Body image")

## Exploring Different Types of Al Agents 

**Types of AI Agents**

* Simple reflex agents
* Model-based reflex agents
* Goal-based agents
* Learning agents

**Simple Reflex Agents** and **Model-Based Reflex Agents**:

### 1.  **Simple Reflex Agents:**

*   **Operation:** React *only* to current percepts (immediate inputs) with no memory of past events.
*   **Requirement:** Work best in **fully observable** environments.
*   **Mechanism:** Follow predefined `condition -> action` rules.
*   **Limitations:**
  *   Cannot learn, adapt, reason, or handle unobservable aspects.
  *   Require increasingly complex rule sets for complex environments (hard to scale/maintain).
*   **Example:** A thermostat turning on heat *only* if current temp < 10°C (fails if a window is open).
*   **Use Cases:** Basic spam filters (keyword matching), simple automated email responders.

> Simple Reflex Agent

![Alt Image Text](../images/chap8_1_2.png "Body image")

Simple reflex agents make decisions based only on current percepts, ignoring history

They work only in fully observable environments

They follow Condition-action rules

- Limited intelligence.
- No knowledge of non-perceptual state aspects.
- Often too large to generate/store.
- Not adaptive to environmental changes

### 2.  **Model-Based Reflex Agents:**


![Alt Image Text](../images/chap8_1_3.png "Body image")

**Model-based agents work in partially observable environments and track situations**

They have two key factors:

- **Model**: Knowledge of how the world works

- **Internal State**: Representation of the current state based on percept history

These agents use their model to make decisions

Updating state requires knowing:

- How the world evolves
- How the agent’s actions affect the world

*   **Operation:** React to current percepts *and* maintain an **internal state** based on past percepts (memory).
*   **Core Components:**
  *   **Model:** Knowledge of "how the world works" (e.g., how actions change the environment).
  *   **Internal State:** Representation of the current world state based on percept history.
*   **Advantage:** More adaptable than simple reflex agents; can handle **partially observable** environments.
*   **Mechanism:** Still use `condition -> action` rules, but conditions can include the internal state.
*   **State Update:** Relies on the model to understand world evolution and action effects.
*   **Use Cases:** Smart thermostats (using history & preferences), smart robotic vacuums (using sensor maps).

### **Key Differences Summarized:**

| Feature          | Simple Reflex Agent        | Model-Based Reflex Agent       |
| :--------------- | :------------------------- | :----------------------------- |
| **Memory**       | None                       | Yes (Internal State)           |
| **Observability**| Requires Full              | Handles Partial                |
| **Adaptability** | None (Rigid Rules)         | Higher (Uses Model & State)    |
| **Complexity**   | Rules bloat in complex env | More complex internally        |
| **Example**      | Basic Thermostat           | Learning Thermostat / Smart Vacuum |

Here's a concise summary of **Goal-Based Agents** and **Learning Agents**:

### 3 **Goal-Based Agents**

- Knowing the current state is not always enough for decision-making 
- Agents need a goal to define desirable outcomes 
- Goal-based agents enhance model-based agents with goal information 
- They select actions to achieve their goal 
- They evaluate action sequences through searching and planning, making them proactive


![Alt Image Text](../images/chap8_1_4.png "Body image")


1.  **Core Function:**  
    *   Plan sequences of actions to achieve **specific goals** (desirable future states).  
    *   Extend model-based agents by incorporating goal information.  
2.  **Key Mechanism:**  
    *   **Searching & Planning:** Evaluate future scenarios to choose actions leading toward the goal.  
    *   **Proactive:** Focus on long-term outcomes rather than immediate reactions.  
3.  **Examples:**  
    *   **Chess AI:** Plans moves to win by evaluating long-term strategies.  
    *   **Logistics Route Optimization:** Plans efficient delivery paths based on priorities (e.g., fuel/time).  

---

### **4 Learning Agents**


![Alt Image Text](../images/chap8_1_5.png "Body image")

A learning agent improves by learning from past experiences

It has four main components:

* **Learning element**: Improves by interacting with the environment
* Critic: Provides feedback on performance.
* Performance element: Selects external actions.
* **Problem generator**: Suggests actions for new experiences.

**Learning agents analyze performance and seek improvements.**


1.  **Core Function:**  
    *   Continuously **adapt and improve** performance through experience.  
    *   Start with basic knowledge and refine over time.
       
2.  **Key Components:**  
    | **Component**       | **Role**                                                                 |  
    |---------------------|--------------------------------------------------------------------------|  
    | **Learning Element** | Improves knowledge/behavior based on environmental feedback.            |  
    | **Critic**          | Evaluates performance against a fixed standard (provides feedback).     |  
    | **Performance Element** | Executes actions (e.g., the agent’s decision-making module).          |  
    | **Problem Generator** | Suggests exploratory actions to gain new, informative experiences.   |  

3.  **Examples:**  
    *   **Recommendation Systems (Netflix/Amazon):** Learn user preferences to refine suggestions.  
    *   **Adaptive Thermostats:** Learn user habits (e.g., schedule, temperature preferences) to auto-adjust.  
