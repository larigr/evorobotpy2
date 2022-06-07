## Modificações nas bibliotecas
---

Primeiro, devemos seguir as instruções contidas no livro base desse simulador para adicionar os experimentos na versão 5 (V5). Após, é preciso modificar algumas bibliotecas, conforme lista abaixo.

---

1. **lib/python3.X/site-packages/pybullet_envs/gym_locomotion_envs.py**

Todos os gym_locomotion_envs.py devem ser modificados (incluindo os adicionados na V5). Primeiro, deve-se adicionar no construtor da classe `WalkerBaseBulletEnv` o atributo `self.distancia = 0`. 

Depois, na linha 82, acima do código `progress = float(self.potential - potential_old)`, deve-se adicionar a seguinte linha `self.distancia = self.robot.walk_target_dist`.