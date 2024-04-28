import os

from colorama import Fore, Style
from langchain_groq import ChatGroq


class GroqProvider:

    def __init__(
        self,
        model,
        temperature,
        max_tokens
    ):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = self.get_api_ley()
        self.llm = self.get_llm_model()
                

    def get_api_ley(self):
        """
        Gets the Groq API Key	
        Returns:

        """
        try:
            api_key = os.environ["GROQ_API_KEY"]
        except:
            raise Exception(
                "Ollama Groq API Key not found. Please set the Groq API Key environment variable.")
        return api_key

   
    def get_llm_model(self):
        # Initializing the chat model
        llm = ChatGroq(
            model_name=self.model,
            temperature=self.temperature,
            groq_api_key = self.api_key
        )

        return llm

    async def get_chat_response(self, messages, stream, websocket=None):
        if not stream:
            # Getting output from the model chain using ainvoke for asynchronous invoking
            
            output = await self.llm.ainvoke(messages)

            return output.content

        else:
            return await self.stream_response(messages, websocket)

    async def stream_response(self, messages, websocket=None):
        paragraph = ""
        response = ""

        # Streaming the response using the chain astream method from langchain
        async for chunk in self.llm.astream(messages):
            content = chunk.content
            if content is not None:
                response += content
                paragraph += content
                if "\n" in paragraph:
                    if websocket is not None:
                        await websocket.send_json({"type": "report", "output": paragraph})
                    else:
                        print(f"{Fore.GREEN}{paragraph}{Style.RESET_ALL}")
                    paragraph = ""
                    
        return response
