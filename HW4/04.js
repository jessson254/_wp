function deepMerge(obj1, obj2)
{
    for(const key in obj2)
    {
        if (obj2[key] && typeof obj2[key] === "object" && !Array.isArray(obj2[key])
        && obj1[key] && typeof obj1[key] === "object")
            {
                deepMerge(obj1[key], obj2[key])
            }
        else
        {
            obj1[key] = obj2[key]
        }
    }
    return obj1
}
const obj1 = { a: 1, b: { x: 2, y: 3 } };
const obj2 = { b: { y: 5, z: 6 }, c: 7 };
console.log(deepMerge(obj1, obj2));
