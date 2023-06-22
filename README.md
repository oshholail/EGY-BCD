<h1 align="center">
  <b>AFDE-Net: Building Change Detection using Attention-Based Feature Differential Enhancement for Satellite Imagery</b><br>
</h1>

[`Shimaa Holail Researchgate`](https://www.researchgate.net/profile/Shimaa-Holail)[`Shimaa Holail Linkedin`](https://www.linkedin.com/in/shimaaholail/), [`Tamer Saleh`](https://www.bu.edu.eg/staff/tamermohamed3), [`Xiongwu Xiao`](http://jszy.whu.edu.cn/xiaoxiongwu1), and [`Deren Li`](http://www.lmars.whu.edu.cn/prof_web/prof_lideren/index.htm)

The train and test code will be released soon. The EGY-BCD dataset is available. 


## Updates
| :zap:        | AFDE-Net has been Published in IEEE Geoscience and Remote Sensing Letters (GRSL). DOI: 10.1109/LGRS.2023.3283505 |
|---------------|:------------------------|



## :speech_balloon: EGY-BCD Dataset Description 
Bi-temporal images in the EGY-BCD dataset are taken from 4 different regions located in Egypt, including New Mansoura, El Galala City, New Cairo, and New Thebes. The figure below shows the building changes in New Mansoura City and New Thebes. Our image data capture time varies from 2017 to 2022. The images feature seasonal changes and different lighting changes in our new dataset, which can help develop effective methods that can mitigate the impact of unrelated changes on real changes.

![image-20230201153142126](./img/MansouraTiba.png)

## :speech_balloon: Network Architecture
An overview of the proposed architecture. (a) is the backbone of ADFE-Net. The node $Xi$ features denotes a convolutional block as shown in (b). The feature differential enhancement FDE is described in (c). (d) is the ensemble spatial-channel attention fusion ESCAF.
![image-20230201153142126](./img/overall.png)


 ## :speech_balloon: <span id="jump">Quantitative and Qualitative Results on the EGY-BCD Dataset</span>
 
### :point_right: Quantitative Results
![image-QuantitativeResult](./img/result2.png)

### :point_right: Qualitative Results

![image-QualitativeResult](./img/result.png)


## :speech_balloon: Requirements

- Python 3.7
- Pytorch 1.7

Please see `requirements.txt` for all the other requirements.


### 🔭 Baselines <a name="baselines"></a>

- [x] Linknet [[paper](https://arxiv.org/abs/1707.03718)]
- [x] UPerNet [[paper](https://arxiv.org/abs/1807.10221)]
- [x] DeepLabV3 [[paper](https://arxiv.org/abs/1706.05587)]
- [x] Unet [[paper](https://arxiv.org/abs/1505.04597)]
- [x] Unet++ [[paper](https://arxiv.org/pdf/1807.10165.pdf)]


#### Encoders <a name="encoders"></a>

Below is a list of encoders used in this work and their pre-trained weights.

<details>
<summary style="margin-left: 25px;">ResNet</summary>
<div style="margin-left: 25px;">

| Encoder   |        Weights        | Params, M |
| --------- | :-------------------: | :-------: |
| resnet50  | imagenet / ssl / swsl |    23M    |
| resnet101 |       imagenet        |    42M    |


</div>
</details>

<details>
<summary style="margin-left: 25px;">RegNet(x/y)</summary>
<div style="margin-left: 25px;">

| Encoder          | Weights  | Params, M |
| ---------------- | :------: | :-------: |
| timm-regnety_120 | imagenet |    49M    |
| timm-regnety_160 | imagenet |    80M    |
| timm-regnety_320 | imagenet |   141M    |


</div>
</details>


## :speech_balloon: <span id="jump">Dataset Preparation</span>

### :point_right: Data Structure

```
"""
EGY-BCD dataset with pixel-level binary labels；
├————train
|      ├———A  
|      ├———B
|      ├———label
|
├————val
|      ├———A  
|      ├———B
|      ├———label
|
├————test
|      ├———A  
|      ├———B
|      ├———label
"""
```

`A`: Images of Time1;
`B`:Images of Time2;
`label`: Ground Truth;
`each file contains the image names (XXXX.png)`


### :truck: Datasets <a name="dataset"></a>

You can download our novel public EGY-BCD dataset through the following link:

- [x] [EGY-BCD][baidu drive](https://pan.baidu.com/s/1UREv4F0DBHgabJW2VScgCA) Passward: (EGYD)


### :page_with_curl: Citing <a name="citing"></a>

```
@ARTICLE{10145434,
  author={Shimaa Holail, Tamer Saleh, Xiongwu Xiao, and Deren Li},
  journal={in IEEE Geoscience and Remote Sensing Letters}, 
  title={AFDE-Net: Building Change Detection Using Attention-Based Feature Differential Enhancement for Satellite Imagery}, 
  year={2023},
  volume={20},
  number={6006405},
  pages={1-5},
  doi={10.1109/LGRS.2023.3283505}}

```
  
### Contact Information
If you have any question about EGY-BCD dataset, please contact shimaaholail@whu.edu.cn


## :speech_balloon: References

Appreciate the work from the following repositories:

- [wenhwu/awesome-remote-sensing-change-detection](https://github.com/wenhwu/awesome-remote-sensing-change-detection)
- [qubvel/segmentation_models.pytorch](https://github.com/qubvel/segmentation_models.pytorch)
- [likyoo/PRCV2021_ChangeDetection_Top3](https://github.com/likyoo/PRCV2021_ChangeDetection_Top3)
- [likyoo/Pytorch-UNet](https://github.com/likyoo/Pytorch-UNet)
- [angup143/disaster_mapping](https://github.com/angup143/disaster_mapping/tree/5bab37700950bb9b5e6af9bbe41a6ab66645bf58)


