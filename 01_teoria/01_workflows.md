# Tipos comuns de Workflows
Existem quatro categorias principais.

## 1 - Validate

A etapa de **Validate** tem como objetivo validar aspectos do código e das alterações realizadas.

Nesse sentido, essa categoria inclui verificações como formatação do código, erros de digitação, qualidade do código, padronização e possíveis problemas detectados por ferramentas de análise estática.

Em geral, essa etapa busca garantir que o código esteja consistente, legível e seguindo os padrões definidos pelo projeto antes de avançar para as próximas fases.


## 2 - Build

A etapa de **Build** está relacionada à geração dos artefatos necessários para executar ou distribuir a aplicação.

Por exemplo, em uma linguagem compilada, o build pode envolver a compilação do código-fonte para gerar um executável. Em outros casos, pode incluir a criação de pacotes, bibliotecas ou imagens de contêiner.

Portanto, essa etapa transforma o código validado em algo que pode ser executado, testado ou implantado.


## 3 - Deploy

A etapa de **Deploy** consiste em levar os artefatos gerados na etapa de build para um ambiente de execução.

Esses artefatos podem ser executáveis, imagens de contêiner, pacotes ou outros arquivos necessários para rodar a aplicação. O objetivo é disponibilizar o sistema em um servidor, serviço em nuvem ou outro ambiente, deixando-o pronto para uso.

Em resumo, deploy significa colocar a aplicação no ar.


## 4 - Repo Automation

A categoria de **Repo Automation** envolve automações relacionadas à manutenção e organização do repositório.

Alguns exemplos são:

- **Release automation**: automação do processo de criação de releases, como o uso da ferramenta `release-please`;
- **Stale Issues/PRs**: identificação e gerenciamento automático de issues e pull requests antigos ou inativos;
- **Dependency upgrades**: atualização automática de dependências do projeto, como ocorre com ferramentas como `renovate`.

Essas automações ajudam a manter o repositório mais organizado, atualizado e fácil de manter.