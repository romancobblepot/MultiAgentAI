# -*- coding: utf-8 -*-
"""Base_Agent.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12CQdGOJJd2dEtvfwV6rqGl6GxQz0kr9m
"""

import openai
from abc import ABC, abstractmethod
from loguru import logger
import os
from dotenv import load_dotenv

load_dotenv("api.env")

openai.api_key = os.getenv("OPENAI_API_KEY")

class AgentBase(ABC):
  def __init__(self,name,max_retries=2,verbose=True):
    self.name = name
    self.max_retries=max_retries
    self.verbose=verbose

  def execute(self,*args,**kwargs):
      pass

  def call_openai(self,messages,temperature=0.7,max_tokens=150):
    retries=0
    while retries<self.max_retries:
      try:
        if self.verbose:
          logger.info(f"[{self.name}] Sending messages to OpenAI:")
          for msg in messages:
            logger.debug(f" {msg['role']}: {msg['content']}")
        response= openai.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        reply =response.choices[0].messages
        if self.verbose:
          logger.info(f"[{self.name}] Received response: {reply}")
        return reply
      except Exception as e:
                  retries +=1
                  logger.error(f"[{self.name}] Error during OpenAI call: {e}. Retry {retries}/{self.max_retries}")
    raise Exception(f"[{self.name}] Failed to get response from OpenAI after {self.max_retries} retries. ")
