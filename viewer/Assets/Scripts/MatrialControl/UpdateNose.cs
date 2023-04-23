using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UpdateNose : MonoBehaviour
{
    public Renderer nRenderer;
    public Renderer nS1Renderer;
    public GameObject nose;
    public GameObject noseS1;

    // Start is called before the first frame update
    void Start()
    {
        nRenderer = nose.GetComponent<Renderer>();
        nS1Renderer = nose.GetComponent<Renderer>();
        nRenderer.material = nS1Renderer.material;
    }

}
