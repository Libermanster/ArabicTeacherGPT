from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

#function that takes in a prompt and returns a response with dialoGPT-small
def get_singal_response(prompt):
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')
    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(new_user_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    # pretty print last ouput tokens from bot
    return tokenizer.decode(chat_history_ids[:, new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)


def createPromptWithHistory(prompt, chat_ids):
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    chat_ids[0] = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_ids[1], chat_ids[0]], dim=-1) if chat_ids[2] > 0 else chat_ids[0]

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_ids[2] += 1
    chat_ids[1] = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    print("chat_ids[0]: {}".format(chat_ids[0]))
    print("chat_ids[1]: {}".format(chat_ids[1]))
    chat_history = []
    chat_history.append(chat_ids[1][::][0])
    print("chat_history: {}".format(tokenizer.decode(torch.cat(chat_history, dim=-1), skip_special_tokens=True)))
    #print("chat_ids[1]: {}".format(tokenizer.decode(torch.cat(chat_ids[1], dim=-1), skip_special_tokens=True)))
    print("chat_ids[2]: {}".format(chat_ids[2]))
    #print("chat_ids[2]: {}".format(tokenizer.decode(torch.cat(chat_ids[2], dim=-1), skip_special_tokens=True)))
    
    return tokenizer.decode(chat_ids[1][:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

