# Eventos que vão desencadear a execução do workflow

1. **push**
Dispara quando alguém envia commits ou tags para o repositório.

2. **pull_request**
Dispara quando há atividade em um Pull Request, como abrir, atualizar, reabrir ou fechar.

3. **pull_request_target**
Dispara por atividade em Pull Request, mas roda no contexto da branch base do repositório.

4. **workflow_dispatch**
Dispara quando alguém executa o workflow manualmente pelo GitHub.

5. **repository_dispatch**
Dispara quando um sistema externo chama a API do GitHub para iniciar o workflow.

6. **schedule**
Dispara em um horário agendado usando cron.

7. **workflow_run**
Dispara quando outro workflow é iniciado, concluído ou solicitado.

8. **workflow_call**
Dispara quando outro workflow chama esse workflow reutilizável.

9. **issues**
Dispara quando há atividade em uma issue, como abrir, editar, fechar ou reabrir.

10. **issue_comment**
Dispara quando alguém comenta em uma issue ou em um Pull Request.

11. **pull_request_review**
Dispara quando alguém envia uma revisão em um Pull Request.

12. **pull_request_review_comment**
Dispara quando alguém comenta em uma linha específica do diff de um Pull Request.

13. **pull_request_review_thread**
Dispara quando uma conversa de revisão em um Pull Request é resolvida ou reaberta.

14. **release**
Dispara quando há atividade em uma release, como criar, publicar, editar ou deletar.

15. **create**
Dispara quando uma branch ou tag é criada.

16. **delete**
Dispara quando uma branch ou tag é deletada.

17. **fork**
Dispara quando alguém faz fork do repositório.

18. **watch**
Dispara quando alguém dá estrela no repositório.

19. **public**
Dispara quando um repositório privado se torna público.

20. **gollum**
Dispara quando uma página da Wiki é criada ou atualizada.

21. **milestone**
Dispara quando há atividade em uma milestone, como criar, editar, fechar ou deletar.

22. **label**
Dispara quando uma label é criada, editada ou deletada.

23. **registry_package**
Dispara quando há atividade em um pacote do GitHub Packages.

24. **branch_protection_rule**
Dispara quando uma regra de proteção de branch é criada, editada ou deletada.

25. **security_advisory**
Dispara quando há atividade em um advisory de segurança do repositório.

26. **check_run**
Dispara quando há atividade em um check run, como criação, conclusão ou nova solicitação.

27. **check_suite**
Dispara quando há atividade em um conjunto de checks.

28. **commit_comment**
Dispara quando alguém comenta diretamente em um commit.

29. **deployment**
Dispara quando um deployment é criado.

30. **deployment_status**
Dispara quando o status de um deployment muda.

31. **discussion**
Dispara quando há atividade em uma discussão, como criar, editar, fechar ou reabrir.

32. **discussion_comment**
Dispara quando alguém comenta em uma discussão.

33. **merge_group**
Dispara quando um Pull Request entra em uma merge queue.

34. **page_build**
Dispara quando o GitHub Pages inicia ou conclui um build.

35. **project**
Dispara quando há atividade em um Project clássico.

36. **project_card**
Dispara quando há atividade em um card de Project clássico.

37. **project_column**
Dispara quando há atividade em uma coluna de Project clássico.

38. **status**
Dispara quando o status de um commit muda.