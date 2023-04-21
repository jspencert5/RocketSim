using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using static UnityEngine.UIElements.UxmlAttributeDescription;
using UnityEngine.PlayerLoop;
using UnityEngine.UI;

public class GraphLoader : MonoBehaviour
{

    void Start()
    {
        GameObject graphs = GameObject.Find("Graphs");

        GameObject graph0 = graphs.transform.Find("Graph").gameObject;
        //graph0.GetComponent<Image>().sprite = Resources.Load<Sprite>("pos");

        GameObject graph1 = graphs.transform.Find("Graph (1)").gameObject;
        //graph1.GetComponent<Image>().sprite = Resources.Load<Sprite>("vel");

        GameObject graph2 = graphs.transform.Find("Graph (2)").gameObject;
        //graph2.GetComponent<Image>().sprite = Resources.Load<Sprite>("acc");
    }
    
}
