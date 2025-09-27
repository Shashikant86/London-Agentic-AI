#!/usr/bin/env python3
"""
Author: Shashi Jagtap (converted original notebook to Python script) 
DSPy Evaluator-Optimizer Tutorial: Joke-Telling AI with GEPA (Ollama Version)

This script demonstrates the evaluator-optimizer pattern in DSPy, building a joke-telling AI
that learns what makes jokes funny through optimization using the GEPA evolutionary optimizer.
This version uses Ollama for local inference - no API keys required!

Key DSPy concepts demonstrated:
- Signatures and predictors
- LLM-as-a-Judge pattern
- GEPA (evolutionary optimizer)
- Chain of thought reasoning
- Few-shot learning
- Evaluation metrics

Prerequisites:
- Ollama installed and running
- llama3.1:8b model pulled: `ollama pull llama3.1:8b`

Original notebook: evaluator-optimizer-in-dspy.ipynb
"""

import dspy
import os
import random
import argparse
from dotenv import load_dotenv

def setup_environment(student_model="ollama_chat/llama3.2:1b", teacher_model="ollama_chat/llama3.1:8b"):
    """Setup DSPy environment and language models using Ollama
    
    Args:
        student_model (str): Model for the student LM (default: llama3.2:1b)
        teacher_model (str): Model for the teacher LM (default: llama3.1:8b)
    """
    # Load environment variables from .env file (optional for Ollama)
    load_dotenv()
    
    # Disable caching to avoid database file issues
    import dspy
    dspy.settings.configure(cache=False)
    
    print(f"Using student model: {student_model}")
    print(f"Using teacher model: {teacher_model}")
    
    # Initialize Ollama language model for student (main model)
    student_lm = dspy.LM(
        model=student_model,
        api_key="",  # Ollama doesn't require API key
        max_tokens=4000,
        temperature=1.0
    )
    
    # Initialize teacher model for optimization (can use same or different model)
    teacher_lm = dspy.LM(
        model=teacher_model,
        api_key="",  # Ollama doesn't require API key
        temperature=1.0,
        max_tokens=4000
    )
    
    return student_lm, teacher_lm

def create_joke_datasets():
    """Create training, validation, and development datasets"""
    random.seed(69)  # Set seed for reproducibility
    
    # Dataset of professional comedian jokes (labeled as funny)
    funny_jokes = [
        {"topic": "Fishing", "joke": "Give a man a fish, and he'll probably follow you home expecting more fish.", "comedian": "Ricky Gervais"},
        {"topic": "Family", "joke": "Where there's a will – there's a relative!", "comedian": "Ricky Gervais"},
        {"topic": "Holidays", "joke": "1st of December, World Aids Day….I don't think it'll ever take off like Christmas.", "comedian": "Ricky Gervais"},
        {"topic": "Drinking", "joke": "I like a drink as much as the next man. Unless the next man is Mel Gibson.", "comedian": "Ricky Gervais"},
        {"topic": "Celebrity", "joke": "It's gonna be a night of partying and heavy drinking. Or as Charlie calls it: breakfast.", "comedian": "Ricky Gervais"},
        {"topic": "Movies", "joke": "It seems like everything this year was three-dimensional, except the characters in The Tourist.", "comedian": "Ricky Gervais"},
        {"topic": "Religion", "joke": "You won't burn in hell. But be nice anyway.", "comedian": "Ricky Gervais"},
        {"topic": "Inspiration", "joke": "My greatest hero is Nelson Mandela. What a man. Incarcerated for 25 years, he was released in 1990 and he hasn't reoffended. I think he's going straight, which shows you prison does work.", "comedian": "Ricky Gervais"},
        {"topic": "Philosophy", "joke": "Remember, when you are dead, you do not know you are dead. It is only painful for others. The same applies when you are stupid.", "comedian": "Ricky Gervais"},
        {"topic": "Life", "joke": "Mondays are fine. It's your life that sucks.", "comedian": "Ricky Gervais"},
        {"topic": "Technology", "joke": "iPhones are Barbie Dolls for grown men. You carry them round, dress them up in little outfits, accessorise, & get a new one every year.", "comedian": "Ricky Gervais"},
        {"topic": "Drinking", "joke": "My father drank so heavily, when he blew on the birthday cake he lit the candles.", "comedian": "Les Dawson"},
        {"topic": "Police", "joke": "I was in my car driving back from work. A police officer pulled me over and knocked on my window. I said, 'One minute I'm on the phone.'", "comedian": "Alan Carr"},
        {"topic": "Overthinking", "joke": "I worry about ridiculous things, you know, how does a guy who drives a snowplough get to work in the morning… that can keep me awake for days.", "comedian": "Billy Connolly"},
        {"topic": "Relationships", "joke": "I used to go out with a giraffe. Used to take it to the pictures and that. You'd always get some bloke complaining that he couldn't see the screen.", "comedian": "Paul Merton"},
        {"topic": "Music", "joke": "Here's a picture of me with REM. That's me in the corner.", "comedian": "Milton Jones"},
        {"topic": "Optimism", "joke": "People say 'Bill, are you an optimist?' And I say, 'I hope so.'", "comedian": "Bill Bailey"},
        {"topic": "Customer Service", "joke": "I rang up British Telecom and said: 'I want to report a nuisance caller.' He said: 'Not you again.'", "comedian": "Tim Vine"},
        {"topic": "Sports", "joke": "If I was an Olympic athlete, I'd rather come in last than win the silver medal. You win the gold, you feel good. You win the bronze, you think, 'at least I got something.' But you win that silver, that's like, 'Congratulations, you almost won! Of all the losers, you came in first! You're the number one loser! No one lost ahead of you!'", "comedian": "Jerry Seinfeld"},
        {"topic": "Identity", "joke": "My star sign is Pyrex. I was a test-tube baby.", "comedian": "Billy Connolly"},
        {"topic": "Marriage", "joke": "I always take my wife morning tea in my pyjamas. But is she grateful? No, she says she'd rather have it in a cup.", "comedian": "Eric Morecambe"},
        {"topic": "Crime", "joke": "Crime in multi-storey car parks. That is wrong on so many different levels.", "comedian": "Tim Vine"},
        {"topic": "Animals", "joke": "Owls haven't got necks, have they? An owl is essentially a one-piece unit.", "comedian": "Ross Noble"},
        {"topic": "Fashion", "joke": "If you arrive fashionably late in Crocs, you're just late.", "comedian": "Joel Dommett"},
        {"topic": "Philosophy", "joke": "I doubt there's a heaven; I think the people from hell have probably bought it for a timeshare.", "comedian": "Victoria Wood"},
        {"topic": "Fitness", "joke": "I said to the gym instructor: \"Can you teach me to do the splits?\", He said: \"How flexible are you?\", I said: \"I can't make Tuesdays.\"", "comedian": "Tommy Cooper"},
        {"topic": "Insurance", "joke": "Do Transformers get car, or life insurance?", "comedian": "Russell Howard"},
        {"topic": "Healthcare", "joke": "A good rule to remember for life is that when it comes to plastic surgery and sushi, never be attracted by a bargain.", "comedian": "Graham Norton"},
        {"topic": "Animals", "joke": "Two monkeys were getting into the bath. One said: 'Oo, oo, oo, aah aah aah.' The other replied: 'Well, put some cold in it then.'", "comedian": "Harry Hill"},
        {"topic": "Dating", "joke": "I like a woman with a head on her shoulders. I hate necks.", "comedian": "Steve Martin"},
        {"topic": "Growing Up", "joke": "I have a lot of growing up to do. I realised that the other day inside my fort.", "comedian": "Zach Galifianakis"},
        {"topic": "Employment", "joke": "I used to work at McDonald's making minimum wage. You know what that means when someone pays you minimum wage? You know what your boss was trying to say? 'Hey, if I could pay you less, I would, but it's against the law.'", "comedian": "Chris Rock"},
        {"topic": "Love", "joke": "Love is like a fart. If you have to force it it's probably s***.", "comedian": "Stephen K. Amos"},
        {"topic": "Convenience", "joke": "I like an escalator because an escalator can never break. It can only become stairs. There would never be an 'Escalator Temporarily Out of Order' sign, only 'Escalator Temporarily Stairs'.", "comedian": "Mitch Hedberg"},
        {"topic": "Beauty", "joke": "My girlfriend is absolutely beautiful. Body like a Greek statue – completely pale, no arms.", "comedian": "Phil Wang"},
        {"topic": "Creation", "joke": "If God had written the Bible, the first line should have been 'It's round.'", "comedian": "Eddie Izzard"},
        {"topic": "Self-Improvement", "joke": "I bought myself some glasses. My observational comedy improved.", "comedian": "Sara Pascoe"},
        {"topic": "Politics", "joke": "Trump's nothing like Hitler. There's no way he could write a book.", "comedian": "Frankie Boyle"},
        {"topic": "Social Class", "joke": "You know you're working class when your TV is bigger than your book case.", "comedian": "Rob Beckett"},
        {"topic": "Conflict", "joke": "Most of my life is spent avoiding conflict. I hardly ever visit Syria.", "comedian": "Alex Horne"},
        {"topic": "Health", "joke": "Life is like a box of chocolates. It doesn't last long if you're fat.", "comedian": "Joe Lycett"},
        {"topic": "Memory", "joke": "Apparently smoking cannabis can affect your short term memory. Well if that's true, what do you think smoking cannabis does?", "comedian": "Mickey P Kerr"},
        {"topic": "Marriage", "joke": "The first time I met my wife, I knew she was a keeper. She was wearing massive gloves.", "comedian": "Alun Cochrane"},
        {"topic": "Childhood", "joke": "As a kid I was made to walk the plank. We couldn't afford a dog.", "comedian": "Gary Delaney"},
        {"topic": "Entertainment", "joke": "I saw a documentary on how ships are kept together. Riveting!", "comedian": "Stewart Francis"},
        {"topic": "Music", "joke": "People who like trance music are very persistent. They don't techno for an answer.", "comedian": "Joel Dommett"},
        {"topic": "Weather", "joke": "Normally you have news, weather and travel. But not on snow day. On a snow day, news is weather is travel.", "comedian": "Michael McIntyre"},
        {"topic": "Sarcasm", "joke": "Someone showed me a photograph of my local MP the other day. 'Would you buy a second-hand car from this man?' they asked. 'Would you buy a second-hand car?' I replied.", "comedian": "Miles Jupp"},
        {"topic": "Learning", "joke": "I'm learning the hokey cokey. Not all of it. But – I've got the ins and outs.", "comedian": "Iain Stirling"},
        {"topic": "Parenting", "joke": "My mother told me, you don't have to put anything in your mouth you don't want to. Then she made me eat broccoli, which felt like double standards.", "comedian": "Sarah Millican"},
        {"topic": "Vengeance", "joke": "My therapist says I have a preoccupation with vengeance. We'll see about that.", "comedian": "Stewart Francis"},
        {"topic": "Family", "joke": "I'm sure wherever my Dad is, he's looking down on us. He's not dead, just very condescending.", "comedian": "Jack Whitehall"},
        {"topic": "Injury", "joke": "The easiest time to add insult to injury is when you're signing somebody's cast.", "comedian": "Demetri Martin"},
        {"topic": "Humor", "joke": "It's really hard to define 'virtue signalling', as I was saying the other day to some of my Muslim friends over a fair-trade coffee in our local feminist bookshop.", "comedian": "Lucy Porter"},
        {"topic": "Creation", "joke": "If we were truly created by God, then why do we still occasionally bite the insides of our own mouths?", "comedian": "Dara Ó Briain"},
        # Add more jokes as needed - truncated for brevity
    ]
    
    # Dataset of generic, unfunny jokes (labeled as not funny)
    unfunny_jokes = [
        {"topic": "Science", "joke": "Why don't scientists trust atoms? Because they make up everything."},
        {"topic": "Field", "joke": "Why did the scarecrow win an award? Because he was outstanding in his field."},
        {"topic": "Animals", "joke": "Why do cows have hooves instead of feet? Because they lactose."},
        {"topic": "Food", "joke": "What do you call fake spaghetti? An impasta."},
        {"topic": "Animals", "joke": "How does a penguin build its house? Igloos it together."},
        {"topic": "Halloween", "joke": "What do you get when you cross a snowman and a vampire? Frostbite."},
        {"topic": "Books", "joke": "Why was the math book sad? It had too many problems."},
        {"topic": "Food", "joke": "What do you call cheese that isn't yours? Nacho cheese."},
        {"topic": "Skeletons", "joke": "Why don't skeletons fight each other? They don't have the guts."},
        {"topic": "Walls", "joke": "What did one wall say to the other wall? I'll meet you at the corner."},
        {"topic": "Transportation", "joke": "Why did the bicycle fall over? It was two-tired."},
        {"topic": "Animals", "joke": "What do you call a bear with no teeth? A gummy bear."},
        {"topic": "Gym", "joke": "Why don't some couples go to the gym? Because some relationships don't work out."},
        {"topic": "Factories", "joke": "What do you call a factory that makes good products? A satisfactory."},
        {"topic": "Golf", "joke": "Why did the golfer bring an extra pair of pants? In case he got a hole in one."},
        {"topic": "Cleaning", "joke": "What did the janitor say when he jumped out of the closet? Supplies!"},
        {"topic": "Animals", "joke": "What do you call a fish with no eyes? Fsh."},
        {"topic": "Charity", "joke": "Why don't oysters donate to charity? Because they are shellfish."},
        {"topic": "Food", "joke": "What did the grape do when it got stepped on? Nothing but let out a little wine."},
        {"topic": "Animals", "joke": "Why was the big cat disqualified from the race? Because it was a cheetah."},
        {"topic": "Fashion", "joke": "What do you call a belt made of watches? A waist of time."},
        {"topic": "Body", "joke": "Why can't your nose be 12 inches long? Because then it would be a foot."},
        {"topic": "Sports", "joke": "Why don't some fish play basketball? Because they are afraid of the net."},
        {"topic": "Animals", "joke": "What do you call a pile of cats? A meowtain."},
        {"topic": "Coffee", "joke": "Why did the coffee file a police report? It got mugged."},
        {"topic": "Weather", "joke": "Why did the stadium get hot after the game? All the fans left."},
        {"topic": "Plates", "joke": "What did one plate say to the other plate? Lunch is on me."},
        {"topic": "Space", "joke": "How do you organize a space party? You planet."},
        {"topic": "Food", "joke": "Why don't eggs tell jokes? They'd crack each other up."},
        {"topic": "Halloween", "joke": "How does a vampire start a letter? Tomb it may concern."},
        {"topic": "Technology", "joke": "Why did the computer go to the doctor? It had a virus."},
        {"topic": "Boomerangs", "joke": "What do you call a boomerang that doesn't come back? A stick."},
        {"topic": "Ghosts", "joke": "Why are ghosts bad at lying? Because you can see right through them."},
        {"topic": "Animals", "joke": "What do you get when you cross a sheep and a kangaroo? A woolly jumper."},
        {"topic": "Food", "joke": "Why did the tomato turn red? Because it saw the salad dressing."},
        # Add more unfunny jokes as needed - truncated for brevity
    ]
    
    # Convert to DSPy format
    dataset = []
    
    # Process funny jokes
    for row in funny_jokes:
        topic, joke, comedian = row["topic"], row["joke"], row["comedian"]
        dataset.append(dspy.Example(topic=topic, comedian=comedian, joke=joke, funny=True).with_inputs("topic", "comedian", "joke"))
    
    # Process unfunny jokes
    for row in unfunny_jokes:
        topic, joke = row["topic"], row["joke"]
        dataset.append(dspy.Example(topic=topic, joke=joke, comedian=None, funny=False).with_inputs("topic", "comedian", "joke"))
    
    # Shuffle the dataset
    random.shuffle(dataset)
    
    # Split into 60% training, 20% validation, 20% development
    num_items = len(dataset)
    train_index = int(0.6 * num_items)
    val_index = int(0.8 * num_items)
    
    trainset = dataset[:train_index]
    valset = dataset[train_index:val_index]
    devset = dataset[val_index:]
    
    print(f"Training set size: {len(trainset)}")
    print(f"Validation set size: {len(valset)}")
    print(f"Development set size: {len(devset)}")
    
    return trainset, valset, devset

def create_comedian_program(student_lm):
    """Create the basic joke generation program"""
    # Define custom instructions for our joke generator
    instructions = """Tell a funny joke about the topic in the style of the comedian"""
    
    # Define input and output fields with descriptions
    fields = {
        "topic": (str, dspy.InputField(desc="The topic of the joke")),
        "comedian": (str, dspy.InputField(desc="The comedian to imitate")),
        "joke": (str, dspy.OutputField(desc="The joke that is being told")),
    }
    
    # Create a signature programmatically
    comedian_signature = dspy.make_signature(
        signature_name="Comedian",
        instructions=instructions,
        signature=fields
    )
    
    # Create a program with our custom signature
    comedian_program = dspy.Predict(comedian_signature)
    comedian_program.set_lm(student_lm)
    
    return comedian_program

def create_audience_judge(student_lm):
    """Create the joke evaluation program using Chain of Thought"""
    # Define custom instructions for our joke judge
    instructions = """You are in the audience at a comedy show and must decide if the joke is funny."""
    
    # Define input and output fields with descriptions
    fields = {
        "topic": (str, dspy.InputField(desc="The topic of the joke")),
        "joke": (str, dspy.InputField(desc="The joke that is being told")),
        "funny": (bool, dspy.OutputField(desc="Whether the joke is funny")),
    }
    
    # Create a signature programmatically
    audience_signature = dspy.make_signature(
        signature_name="Audience",
        instructions=instructions,
        signature=fields
    )
    
    audience_program = dspy.ChainOfThought(audience_signature)
    audience_program.set_lm(student_lm)
    
    return audience_program

def exact_match(gold: dspy.Example, pred: dspy.Prediction, trace=None, pred_name=None, pred_trace=None):
    """Check if the predicted 'funny' label matches the gold answer"""
    return gold.funny == pred.funny

def create_audience_metric(optimized_audience):
    """Create LLM-as-a-Judge metric for evaluating jokes"""
    def audience_metric(gold: dspy.Example, pred: dspy.Prediction, trace=None, pred_name=None, pred_trace=None):
        """Check if the joke is funny or not using the llm-as-a-judge technique"""
        response = optimized_audience(topic=gold.topic, joke=pred.joke)
        # Return feedback for the GEPA optimizer
        return dspy.Prediction(score=response.funny, feedback=response.reasoning)
    
    return audience_metric

def optimize_with_gepa(program, trainset, valset, metric, teacher_lm, max_evals=1):
    """Optimize a program using GEPA evolutionary optimizer"""
    optimizer = dspy.GEPA(
        metric=metric,
        max_full_evals=max_evals,
        num_threads=1,  # Reduced from 16 to avoid file descriptor limits
        track_stats=True,
        use_merge=False,
        reflection_lm=teacher_lm,
    )
    
    optimized_program = optimizer.compile(
        program,
        trainset=trainset,
        valset=valset,
    )
    
    return optimized_program

def test_comedian_program(comedian_program):
    """Test the comedian program with a sample input"""
    output = comedian_program(topic="AI engineering", comedian="Ricky Gervais")
    print(f"Generated joke: {output.joke}")
    return output

def export_optimized_prompt(optimized_comedian):
    """Export the optimized prompt to OpenAI format"""
    prompt = {
        name: dspy.ChatAdapter().format(
            p.signature,
            demos=p.demos,
            inputs={k: f"{{{k}}}" for k in p.signature.input_fields},
        )
        for name, p in optimized_comedian.named_predictors()
    }['self']
    
    print("System prompt:")
    print(prompt[0]["content"])
    return prompt

def main(student_model="ollama_chat/llama3.2:1b", teacher_model="ollama_chat/llama3.1:8b"):
    """Main execution function demonstrating the evaluator-optimizer pattern
    
    Args:
        student_model (str): Model for the student LM
        teacher_model (str): Model for the teacher LM  
    """
    print("=== DSPy Evaluator-Optimizer Tutorial (Ollama Version) ===")
    print("Building a joke-telling AI with GEPA optimization using local models\n")
    
    # Setup environment
    print("1. Setting up Ollama environment...")
    print(f"   Using student model: {student_model}")
    print(f"   Using teacher model: {teacher_model}")
    print("   Make sure Ollama is running and models are pulled")
    student_lm, teacher_lm = setup_environment(student_model, teacher_model)
    
    # Test language model
    test_response = student_lm("Hello")
    print(f"LM test: {test_response[0]}\n")
    
    # Create datasets
    print("2. Creating datasets...")
    trainset, valset, devset = create_joke_datasets()
    print()
    
    # Create basic comedian program
    print("3. Creating comedian program...")
    comedian_program = create_comedian_program(student_lm)
    test_comedian_program(comedian_program)
    print()
    
    # Create audience judge
    print("4. Creating audience judge...")
    audience_program = create_audience_judge(student_lm)
    
    # Test audience judge
    result = audience_program(topic=trainset[0].topic, joke=trainset[0].joke)
    print(f"Judge reasoning: {result.reasoning}")
    print(f"Judge prediction: {result.funny}")
    print(f"Ground truth: {trainset[0].funny}\n")
    
    # Evaluate basic audience judge
    print("5. Evaluating basic audience judge...")
    evaluate_audience = dspy.Evaluate(
        metric=exact_match,
        devset=devset,
        num_threads=1,  # Reduced from 16 to avoid file descriptor limits
        display_progress=True,
        display_table=5
    )
    
    baseline_judge_score = evaluate_audience(audience_program)
    print(f"Basic judge accuracy: {baseline_judge_score}%\n")
    
    # Add few-shot examples to audience judge
    print("6. Adding few-shot examples to audience judge...")
    fewshot_optimizer = dspy.LabeledFewShot(k=8)
    fewshot_audience = fewshot_optimizer.compile(student=audience_program, trainset=trainset)
    fewshot_audience.set_lm(student_lm)
    
    fewshot_score = evaluate_audience(fewshot_audience)
    print(f"Few-shot audience accuracy: {fewshot_score}%\n")
    
    # Optimize audience judge with GEPA
    print("7. Optimizing audience judge with GEPA...")
    try:
        optimized_audience = optimize_with_gepa(
            fewshot_audience, trainset, valset, exact_match, teacher_lm
        )
        
        opt_audience_score = evaluate_audience(optimized_audience)
        print(f"Optimized audience accuracy: {opt_audience_score}%\n")
    except Exception as e:
        print(f"Error during audience optimization: {e}")
        print("Using fewshot audience instead of optimized version\n")
        optimized_audience = fewshot_audience
        opt_audience_score = fewshot_score
    
    # Create LLM-as-a-Judge metric for comedian evaluation
    print("8. Creating LLM-as-a-Judge metric...")
    audience_metric = create_audience_metric(optimized_audience)
    
    # Filter datasets for jokes with comedians
    comedian_trainset = [ex for ex in trainset if hasattr(ex, 'comedian') and ex.comedian]
    comedian_valset = [ex for ex in valset if hasattr(ex, 'comedian') and ex.comedian]
    comedian_devset = [ex for ex in devset if hasattr(ex, 'comedian') and ex.comedian]
    
    print(f"Comedian training set size: {len(comedian_trainset)}")
    print(f"Comedian validation set size: {len(comedian_valset)}")
    print(f"Comedian development set size: {len(comedian_devset)}\n")
    
    # Evaluate basic comedian
    print("9. Evaluating basic comedian...")
    evaluate_comedian = dspy.Evaluate(
        metric=audience_metric,
        devset=comedian_devset,
        num_threads=1,  # Reduced from 16 to avoid file descriptor limits
        display_progress=True,
        display_table=5
    )
    
    baseline_comedian_score = evaluate_comedian(comedian_program)
    print(f"Basic comedian accuracy: {baseline_comedian_score}%\n")
    
    # Add few-shot examples to comedian
    print("10. Adding few-shot examples to comedian...")
    fewshot_comedian = fewshot_optimizer.compile(student=comedian_program, trainset=trainset)
    fewshot_comedian.set_lm(student_lm)
    
    fewshot_comedian_score = evaluate_comedian(fewshot_comedian)
    print(f"Few-shot comedian accuracy: {fewshot_comedian_score}%\n")
    
    # Optimize comedian with GEPA
    print("11. Optimizing comedian with GEPA...")
    try:
        optimized_comedian = optimize_with_gepa(
            fewshot_comedian, trainset, valset, audience_metric, teacher_lm
        )
        
        opt_comedian_score = evaluate_comedian(optimized_comedian)
        print(f"Optimized comedian accuracy: {opt_comedian_score}%\n")
    except Exception as e:
        print(f"Error during comedian optimization: {e}")
        print("Using fewshot comedian instead of optimized version\n")
        optimized_comedian = fewshot_comedian
        opt_comedian_score = fewshot_comedian_score
    
    # Test optimized comedian
    print("12. Testing optimized comedian...")
    final_output = optimized_comedian(topic="AI engineering", comedian="Ricky Gervais")
    print(f"Optimized joke: {final_output.joke}\n")
    
    # Export optimized prompt
    print("13. Exporting optimized prompt...")
    export_optimized_prompt(optimized_comedian)
    
    # Summary
    print("\n=== RESULTS SUMMARY ===")
    print(f"Basic audience judge accuracy: {baseline_judge_score}%")
    print(f"Optimized audience judge accuracy: {opt_audience_score}%")
    print(f"Basic comedian accuracy: {baseline_comedian_score}%")
    print(f"Optimized comedian accuracy: {opt_comedian_score}%")
    
    return {
        'optimized_comedian': optimized_comedian,
        'optimized_audience': optimized_audience,
        'scores': {
            'baseline_judge': baseline_judge_score,
            'optimized_judge': opt_audience_score,
            'baseline_comedian': baseline_comedian_score,
            'optimized_comedian': opt_comedian_score
        }
    }

def parse_args():
    """Parse command line arguments for model configuration"""
    parser = argparse.ArgumentParser(
        description="DSPy GEPA Demo with Local Ollama Models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  # Default models (recommended for most systems)
  python evaluator_optimizer_dspy.py
  
  # Larger models for better performance (requires more RAM)
  python evaluator_optimizer_dspy.py --student llama3.1:8b --teacher qwen3:8b
  
  # High-performance models (requires 64GB+ RAM)
  python evaluator_optimizer_dspy.py --student gpt-oss:20b --teacher gpt-oss:120b
        """
    )
    
    parser.add_argument(
        "--student", 
        default="llama3.2:1b",
        help="Student model name (default: llama3.2:1b)"
    )
    
    parser.add_argument(
        "--teacher", 
        default="llama3.1:8b",
        help="Teacher model name (default: llama3.1:8b)"
    )
    
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="List available Ollama models and exit"
    )
    
    return parser.parse_args()

def list_available_models():
    """List available Ollama models"""
    try:
        import subprocess
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, check=True)
        print("Available Ollama models:")
        print(result.stdout)
    except subprocess.CalledProcessError:
        print("Error: Could not list Ollama models. Make sure Ollama is installed and running.")
    except FileNotFoundError:
        print("Error: Ollama not found. Please install Ollama first.")

if __name__ == "__main__":
    # Parse command line arguments
    args = parse_args()
    
    # List models if requested
    if args.list_models:
        list_available_models()
        exit(0)
    
    # Prepare model names with ollama_chat prefix
    student_model = f"ollama_chat/{args.student}"
    teacher_model = f"ollama_chat/{args.teacher}"
    
    print(f"Starting DSPy GEPA Demo...")
    print(f"Student model: {args.student}")
    print(f"Teacher model: {args.teacher}")
    print()
    
    # Install required packages (uncomment if needed)
    # import subprocess
    # subprocess.run(["pip", "install", "dspy", "python-dotenv", "pandas"], check=True)
    
    import asyncio
    
    try:
        results = main(student_model, teacher_model)
    finally:
        # Clean up any remaining event loops to prevent warnings
        try:
            import asyncio
            try:
                loop = asyncio.get_running_loop()
                if not loop.is_closed():
                    loop.close()
            except RuntimeError:
                # No running loop, try to get current one
                try:
                    loop = asyncio.get_event_loop()
                    if not loop.is_closed():
                        loop.close()
                except RuntimeError:
                    pass
        except Exception:
            pass