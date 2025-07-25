public class DynamicArray{
  int capacity = 2;
  int size = 0;
  Object[] data;

  public DynamicArray(){
    data = new Object[capacity];
    printing();
  }

  public void printing(){
    System.out.println("The value of size is " + this.size);
  }

  public DynamicArray(int capacity){
    this.capacity = capacity;
    data = new Object[capacity];
  }

  public void add(Object data){
    // System.out.println("The value of size is " +size);
    if(size >= capacity){
      grow();
    }

    this.data[size] = data;
    size++;
  }

  public void insert(int index, Object item){
    if(this.size >= this.capacity){
      grow();
    }

    if(index >= capacity ){
      System.err.println("Index out of bound kindly ... max index is " + (capacity() - 1) + ".");
      return;
    }

    for(int i = this.size() -1; i >= index; --i){
      this.data[i + 1] = this.data[i];
      if(i == index){
        this.data[i] = item;
        // System.out.println("data inserted in to the arraylist.");
        break;
      }
    }
    size++;
  }

  public void delete(Object item){
    if(!search(item)){
      System.out.println("No such element ....");
      return;
    }
    int index = -1;
    for(int i = 0; i < this.size; ++i){
      if(data[i] == item){
        index = i;
        break;
      }
    }
    for(int i = index; i < size - 1; ++i){
      data[i] = data[i + 1];
    }
    size--;

    if(size < (this.capacity / 2) + 1){
      this.shrink();
    }
  }
  public Object poll(){
    if(this.size < 0 ){
      return null;
    }

    Object item = data[size];
    this.size--;

    if(size < (this.capacity / 2) + 1){
      this.shrink();
    }

    return item;
  }

  public void shrink(){
    int new_capacity = (int)(this.capacity / 2) + 1;
    Object[] new_array = new Object[new_capacity];
    for(int i = 0; i < this.size ; ++i){
      new_array[i] = this.data[i];
    }

    this.data = new_array;
    this.capacity = new_capacity;
  }

  public boolean search(Object item){
    for(int i = 0; i < this.size; ++i){
      if(this.data[i] == item){
        return true;
      }
    }
    return false;
  }

  public int capacity(){
    return this.capacity;
  }

  public int size(){
    return this.size;
  }

  public boolean isEmpty(){
    return size == 0;
  }

  @Override
  public String toString(){
    String result = "";
    for(int i = 0; i < this.size; i++){
      result = result + "" + this.data[i] + ", "; 
    }
    if(result != ""){
      result = "[" + result.substring(0,result.length() - 2) + "]";
    }else{
      result = "[ ]";
    }
    return result;
  }

  public void grow(){
    int new_capacity = (int)(capacity * 2);
    Object[] new_array = new Object[new_capacity];

    for(int i = 0; i < this.capacity; ++i){
      new_array[i] = this.data[i];
    }

    this.data = new_array;
    this.capacity = new_capacity;
  }
}
