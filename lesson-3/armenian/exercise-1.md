## Առաջադրանք 1: Պատրաստում ենք տվյալները

### Քայլ 0:
Ստեղծի նոր Graph օբյեկտ ([documentation](https://www.tensorflow.org/api_docs/python/tf/Graph)). Օգտագործի "with" ու as_default() միասին որպեսզի բոլոր թենզորները ու գործողությունները ավելացվեն ստեղծված գրաֆին (ու ոչ թե հիմնական գրաֆին), [documentation](https://www.tensorflow.org/api_docs/python/tf/Graph#as_default)).

### Քայլ 1:
Ստեղծի Python list որի մեջ կպահենք input առանձնահատկությունները (պարապած ժամեր, քնած ժամեր)։ Այդ տվյալները README ֆայլի մեջ էն։ Զանգվածի չափը 10x2 է (10 օրինակ ու 2 առանձնահատկություն)։

### Քայլ 2:
Ստեղծի Python list որի մեջ կպահենք output պատասխանները (գնահատականները)։ Այդ տվյալները README ֆայլի մեջ էն։ Զանգվածի չափը 10x1 է (10 օրինակ ու 1 գնահատական)։

### Քայլ 3:
Ստեղծի tensorflow placeholder (տեղապահ) որի մեջ կպահենք float32 տիպի տվյալներ ([documentation](https://www.tensorflow.org/versions/r0.11/api_docs/python/io_ops/placeholders)).

### Քայլ 4:
Ստեղծի մի հատ էլ tensorflow placeholder որի մեջ ևս կպահենք float32 **output** տվյալներ։

### Քայլ 5:
Այս տեղապահները օգտագործելու ենք որպեսզի նեյրոնային ցանցը սնենք տվյալներով։ tf.Session-ի run() ֆունկցիան ունի feed_dict պարամետր ([documentation](https://www.tensorflow.org/api_docs/python/tf/Session#run)). Պարամետրին պիտի տանք Python dictionary ([documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries))։ Ստեղծի dictionary ու մեջը պահի հետևյալ երկու key-value զույգերը։
* Առաջինի key-ն **input** թենզորն է որը ստեղծել ենք **Քայլ 3**-ում։ Առաջինի value-ն Python list-ն է որը ստեղծել ենք **Քայլ 1**-ում.
* Երկրորդի key-ն **output** թենզորն է որը ստեղծել ենք **Քայլ 4**-ում։ Երկրորդի value-ն Python list-ն է որը ստեղծել ենք **Քայլ 2**-ում.

Այս dictionary-ն հետո կօգտագործենք ուսուցման ու ստուգման փուլերում։

### Քայլ 6:
**input** և **output** թենզորները պետք է նորմալիզացնել (որպեսզի արժեքները ընկնեն 0-1 շրջանակներում). Ամեն առանձնահատկության համար, պիտի գտնենք մաքսիմալ արժեքը ու բոլոր արժեքները բաժանենք այդ արժեքին։

* Օգտագործի reduce_max() ֆունկցիան որ գտնես մաքսիմալ արժեքը ([documentation](https://www.tensorflow.org/api_docs/python/tf/reduce_max)). Այս քայլը կստեղծի 1x2 չափանի թենզոր։

* **Քայլ 3**-ի **input** թենզորը բաժանի reduce_max()-ի արդյունքին Արդյունքում կստանանք նորմալիզացված արժեքներ։

### Քայլ 7:
**Քայլ 6**-ը կրկնի որպեսզի **output** թենզորը նորմալիզացվի։