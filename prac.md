
## Balanced the dataset

One approach to addressing imbalanced datasets is to oversample the minority class. The simplest approach involves duplicating examples in the minority class, although these examples don’t add any new information to the model. Instead, new examples can be synthesized from the existing examples. This is a type of data augmentation for the minority class and is referred to as the Synthetic Minority Oversampling Technique, or SMOTE for short.

In this tutorial, you will discover the SMOTE for oversampling imbalanced classification datasets.

After completing this tutorial, you will know:

- How the SMOTE synthesizes new examples for the minority class.
- How to correctly fit and evaluate machine learning models on SMOTE-transformed training datasets.
- How to use extensions of the SMOTE that generate synthetic examples along the class decision boundary.

## Feature Extraction

```
# gitignore template for InforCRM (formerly SalesLogix)
# website: https://www.infor.com/product-summary/cx/infor-crm/
#
# Recommended: VisualStudio.gitignore

# Ignore model files that are auto-generated
ModelIndex.xml
ExportedFiles.xml
```


## Selecting the model

https://github.com/brightmart/text_classification/edit/master/README.md

## Evaluating the model

Performance
-------------------------------------------------------------------------

(mulit-label label prediction task,ask to prediction top5, 3 million training data,full score:0.5)

Model   | fastText|TextCNN|TextRNN| RCNN | HierAtteNet|Seq2seqAttn|EntityNet|DynamicMemory|Transformer
---     | ---     | ---   | ---   |---   |---         |---        |---      |---          |----
Score   | 0.362   |  0.405| 0.358 | 0.395| 0.398      |0.322      |0.400    |0.392        |0.322
Training| 10m     |  2h   |10h    | 2h   | 2h         |3h         |3h       |5h           |7h
--------------------------------------------------------------------------------------------------
 


