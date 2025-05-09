.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is h LHashTable; from Label2 to Label3
	new HashTable
	dup
	bipush 10
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	dup
	iconst_5
	iconst_0
	iastore
	dup
	bipush 6
	iconst_0
	iastore
	dup
	bipush 7
	iconst_0
	iastore
	dup
	bipush 8
	iconst_0
	iastore
	dup
	bipush 9
	iconst_0
	iastore
	invokespecial HashTable/<init>(I[I)V
	astore_1
.var 2 is key I from Label2 to Label3
	iconst_5
	istore_2
.var 3 is index I from Label2 to Label3
	aload_1
	iload_2
	invokevirtual HashTable/hash(I)I
	istore_3
	aload_1
	getfield HashTable/table [I
	iload_3
	iload_2
	iastore
	iconst_0
.var 4 is i I from Label2 to Label3
	istore 4
Label6:
	iload 4
	aload_1
	getfield HashTable/size I
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_1
	getfield HashTable/table [I
	iload 4
	iaload
	invokestatic io/putIntLn(I)V
Label10:
Label4:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label6
Label5:
Label3:
Label1:
	return
.limit stack 19
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
