# config file
import json
import os


class Config:
    """Config class for GPT Researcher."""

    def __init__(self, config_file: str = None):
        """Initialize the config class."""
        self.config_file = config_file if config_file else os.getenv('CONFIG_FILE')
        self.retriever = os.getenv('SEARCH_RETRIEVER', "tavily")
        self.embedding_provider = os.getenv('EMBEDDING_PROVIDER', 'openai')
        self.llm_provider = os.getenv('LLM_PROVIDER', "openai")
        self.fast_llm_model = os.getenv('FAST_LLM_MODEL', "gpt-3.5-turbo-16k")
        self.smart_llm_model = os.getenv('SMART_LLM_MODEL', "gpt-4-turbo")
        self.fast_token_limit = int(os.getenv('FAST_TOKEN_LIMIT', 2000))
        self.smart_token_limit = int(os.getenv('SMART_TOKEN_LIMIT', 4000))
        self.browse_chunk_max_length = int(os.getenv('BROWSE_CHUNK_MAX_LENGTH', 8192))
        self.summary_token_limit = int(os.getenv('SUMMARY_TOKEN_LIMIT', 700))
        self.temperature = float(os.getenv('TEMPERATURE', 0.55))
        self.user_agent = os.getenv('USER_AGENT', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                                   "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0")
        self.max_search_results_per_query = int(os.getenv('MAX_SEARCH_RESULTS_PER_QUERY', 5))
        self.memory_backend = os.getenv('MEMORY_BACKEND', "local")
        self.total_words = int(os.getenv('TOTAL_WORDS', 1000))
        self.report_format = os.getenv('REPORT_FORMAT', "APA")
        self.max_iterations = int(os.getenv('MAX_ITERATIONS', 3))
        self.agent_role = os.getenv('AGENT_ROLE', None)
        self.scraper = os.getenv("SCRAPER", "bs")
        self.max_subtopics = os.getenv("MAX_SUBTOPICS", 3)

        self.load_config_file()

    def load_config_file(self) -> None:
        """Load the config file."""
        if self.config_file is None:
            return None
        with open(self.config_file, "r") as f:
            config = json.load(f)
        for key, value in config.items():
            self.__dict__[key] = value

    def __str__(self):
        config_str = f"retriever: {self.retriever}\n"
        config_str += f"embedding_provider: {self.embedding_provider}\n"
        config_str += f"llm_provider: {self.llm_provider}\n"
        config_str += f"fast_llm_model: {self.fast_llm_model}\n"
        config_str += f"smart_llm_model: {self.smart_llm_model}\n"
        config_str += f"fast_token_limit: {self.fast_token_limit}\n"
        config_str += f"smart_token_limit: {self.smart_token_limit}\n"
        config_str += f"browse_chunk_max_length: {self.browse_chunk_max_length}\n"
        config_str += f"summary_token_limit: {self.summary_token_limit}\n"
        config_str += f"temperature: {self.temperature}\n"
        config_str += f"user_agent: {self.user_agent}\n"
        config_str += f"max_search_results_per_query: {self.max_search_results_per_query}\n"
        config_str += f"memory_backend: {self.memory_backend}\n"
        config_str += f"total_words: {self.total_words}\n"
        config_str += f"report_format: {self.report_format}\n"
        config_str += f"max_iterations: {self.max_iterations}\n"
        config_str += f"agent_role: {self.agent_role}\n"
        config_str += f"scraper: {self.scraper}\n"
        config_str += f"max_subtopics: {self.max_subtopics}\n"
        return config_str
