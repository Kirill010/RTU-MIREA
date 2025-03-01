using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ColorCollider : MonoBehaviour
{

    private float timer;
    private bool flag;
    void Start()
    {
        timer = 0f;
        flag = false;
    }

    void Update()
    {
        if (flag && timer <= 1f)
        {
            turnToRed();
        }
        else if (!flag && timer > 0f)
        {
            turnTowhite();
        }
    }
        private void OnCollisionEnter(Collision collision)
        {
            flag = true;
        }
    
        private void OnCollisionExit(Collision collision)
        { 
            flag = false; 
        }
        private void turnToRed()
        {
            timer += Time.deltaTime * 0.001F;
            GetComponent<MeshRenderer>().material.color = Color.Lerp(GetComponent<MeshRenderer>().material.color, Color.red, timer);
        }
    
    private void turnTowhite()
    {
        timer -= Time.deltaTime * 0.001F;
        GetComponent<MeshRenderer>().material.color = Color.Lerp(GetComponent<MeshRenderer>().material.color, Color.white, timer);
    }
    
}
