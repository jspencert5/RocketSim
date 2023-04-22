using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class S2RocketMatController : MonoBehaviour
{
    [SerializeField] private Material[] materialsNose;
    [SerializeField] private Material[] materialsBody;
    [SerializeField] private Material[] materialsThrust;

    private int nVal = NoseMatController.matVal;
    private int bVal = BodyMatController.matVal;
    private int tVal = ThrustMatController.matVal;

    public Renderer noseRenderer;
    public GameObject nose;
    public Renderer bodyRenderer;
    public GameObject body;
    public Renderer thrustRenderer;
    public GameObject thrust;

    // Start is called before the first frame update
    void Start()
    {
        noseRenderer = nose.GetComponent<Renderer>();
        bodyRenderer = body.GetComponent<Renderer>();
        thrustRenderer = thrust.GetComponent<Renderer>();

        noseRenderer.material = materialsNose[nVal];
        bodyRenderer.material = materialsBody[bVal];
        thrustRenderer.material = materialsThrust[tVal];
    }
}
