# 🌍 AI Translation App

A multilingual translation application built with **FastAPI**, **Streamlit**, and **LangChain**. The application translates English text into **German**, **French**, and **Persian** using Large Language Models (LLMs).

---

## ✨ Features

- Translate English text into:
  - 🇩🇪 German
  - 🇫🇷 French
  - 🇮🇷 Persian
- FastAPI backend
- Streamlit user interface
- LangChain PromptTemplate
- Support for multiple LLM providers
- Easily switch between cloud and local models

---

## 🛠 Technologies

- Python
- FastAPI
- Streamlit
- LangChain
- Ollama
- Hugging Face Inference API
- Prompt Engineering

---

## 🤖 Supported LLM Providers

### 1. Hugging Face Inference API

**Model**

- Qwen/Qwen2.5-7B-Instruct

**Advantages**

- High-quality translations
- More natural and fluent responses
- Better contextual understanding

**Requirements**

- Hugging Face account
- Hugging Face API Token

**Note**

Depending on your usage, Hugging Face Inference Providers may require available inference credits. During development, the free monthly credits were exhausted, resulting in the following error:

```text
402 Payment Required
```

---

### 2. Ollama (Local LLM)

**Model**

- qwen2.5:3b

**Advantages**

- Runs completely offline
- No API costs
- No internet connection required
- Easy local deployment

**Limitations**

- Translation quality was lower than the Hugging Face model used in this project.
- Performance depends on the hardware available on the local machine.

---

## 📊 Comparison

| Feature | Hugging Face | Ollama |
|----------|--------------|---------|
| Internet Required | ✅ | ❌ |
| API Token | ✅ | ❌ |
| Additional Credits May Be Required | ✅ | ❌ |
| Offline | ❌ | ✅ |
| Translation Quality (This Project) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## 📝 Evaluation Notes

This project was tested using two different LLM providers.

The Hugging Face model (**Qwen2.5-7B-Instruct**) produced more accurate and natural translations than the local Ollama model (**qwen2.5:3b**).

However, this comparison should **not** be considered a general comparison between **Hugging Face** and **Ollama**.

The local model was limited to **Qwen2.5:3b** because of the available system RAM. Larger local models such as **Qwen2.5:7b** or newer models may provide significantly better translation quality but require more computational resources.

Therefore, the comparison in this project reflects the specific models and hardware configuration used during development.

---

## 🚀 Future Improvements

- Support more languages
- Translation history
- Language auto-detection
- Docker deployment
- Configuration file for selecting LLM providers
- Support additional local and cloud models

---

## 📷 Project Architecture

```
Streamlit
      │
      ▼
FastAPI
      │
      ▼
 LangChain
      │
      ├──────────────┐
      ▼              ▼
 Hugging Face     Ollama
   (Cloud)         (Local)
```

---

## 📌 Disclaimer

The purpose of this project is to learn and compare different LLM deployment approaches using the same application architecture. The reported translation quality reflects the models and environment used during development and should not be interpreted as a benchmark of all Hugging Face or Ollama models.