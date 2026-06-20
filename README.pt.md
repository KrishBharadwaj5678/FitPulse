[English](README.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [Русский](README.ru.md)

# 🏋️‍♂️ FitPulse

**FitPulse** é um aplicativo de monitoramento fitness alimentado por inteligência artificial que utiliza visão computacional para detectar flexões em tempo real, contar repetições, acompanhar o ritmo do treino, salvar o histórico de exercícios em Excel e gerar gráficos de desempenho.

![FitPulseDemo](https://github.com/KrishBharadwaj5678/FitPulse/raw/main/FitPulseDemo.gif)

## 🚀 Funcionalidades

| Funcionalidade                       | Descrição                                                       |
| ------------------------------------ | --------------------------------------------------------------- |
| 🎯 Detecção de Flexões em Tempo Real | Detecta movimentos de flexão usando estimativa de pose          |
| 🔢 Contagem Automática de Repetições | Conta as flexões concluídas com precisão                        |
| ⏱️ Monitoramento do Ritmo do Treino  | Mede o tempo gasto em cada flexão                               |
| ⚠️ Sistema de Alerta de Postura      | Notifica o usuário quando o alinhamento corporal está incorreto |
| 📈 Barra de Progresso                | Exibe o progresso em direção à meta do treino                   |
| 🔊 Feedback Sonoro                   | Reproduz um som a cada repetição concluída                      |
| 📄 Registro de Dados em Excel        | Salva automaticamente o histórico das sessões de treino         |
| 📊 Gráficos de Desempenho            | Exibe análises e estatísticas após o treino                     |
| 📷 Rastreamento por Câmera ao Vivo   | Monitora exercícios diretamente pela webcam                     |
| 📹 Suporte a Arquivos de Vídeo       | Analisa treinos a partir de vídeos gravados                     |
| 🖼️ Exportação de Gráficos em PNG    | Salva gráficos como arquivos de imagem                          |
| 🎨 Interface Limpa                   | Design simples e amigável ao usuário                            |

---

## 🛠 Tecnologias Utilizadas

| Tecnologia               | Finalidade                                     |
| ------------------------ | ---------------------------------------------- |
| 🐍 Python                | Linguagem principal de programação             |
| 🤖 Ultralytics YOLO Pose | Modelo de detecção da pose humana              |
| 🎥 OpenCV                | Processamento de vídeo e exibição da interface |
| 🔢 NumPy                 | Cálculo de ângulos e operações com arrays      |
| 🔊 Pygame                | Sistema de feedback sonoro                     |
| 📄 OpenPyXL              | Criação e atualização de arquivos Excel        |
| 📊 Matplotlib            | Geração e visualização de gráficos             |

---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório

```bash id="d8m4qp"
git clone https://github.com/KrishBharadwaj5678/FitPulse.git
```

### 2️⃣ Acessar o diretório do projeto

```bash id="k3x9ab"
cd FitPulse
```

### 3️⃣ Instalar as dependências

```bash id="v2n7lm"
pip install -r requirements.txt
```

## 4️⃣ Executar o aplicativo

### 📹 Modo de Rastreamento por Vídeo

```bash id="p7q2za"
python main.py
```

#### OU

### 📷 Modo de Rastreamento por Câmera ao Vivo

```bash id="m4v8cd"
python liveTracking.py
```
