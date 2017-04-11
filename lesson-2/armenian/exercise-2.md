## Առաջադրանք 2: Գրաֆի պատկերացումը TensorBoard ծրագրով

### Քայլ 1:
Ստեղծիր ամփոփիչ ֆայլ գրող ([documentation](https://www.tensorflow.org/api_docs/python/tf/summary/FileWriter)) և վերագրիր **graph_writer**-ին. **graph** պարամետրին տուր default graph օբյեկտը ([documentation](https://www.tensorflow.org/api_docs/python/tf/get_default_graph))։ Կոնստրուկտորին պետք է նաև պանակի անուն, որը կստեղծվի ու ամփոփիչ ֆայլերի կպահի իր մեջ։

### Քայլ 2:
TensorBoard ծրագրին սկիզբ տուր հետևյալ հրամանով ([documentation](https://www.tensorflow.org/get_started/summaries_and_tensorboard#launching_tensorboard)). **Տեղապահը փոխիր ու տեղը օգտագործիր քո ընտրած պանակի անունը**: Քանի որ բոլորը կպնում են նույն սերվերին, պետք է նաև հստակեցնել թե որ port-ն եք ուզում գործածել։ Փորձիր 6006-ից սկցված թվեր մինչև բաց port գտնես։

```bash
> tensorboard --logdir=[REPLACE-THIS-WITH-SUBDIRECTORY-NAME] --port=6006
```

### Քայլ 3:
Կտեսնես հետևյալը տերմինալի մեջ:

```bash
Starting TensorBoard 39 on port 6006
(You can navigate to http://127.0.1.1:6006)
```

Բացիր նշված էջը (օրինակ http://127.0.1.1:6006/) որպեսզի տեսնես TensorBoard բարձակը. Բացիր Graphs tab-ը ու կտեսնես քո ստեղծած գրաֆը։