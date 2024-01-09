
#ifndef OBJECT_H
#define OBJECT_H
struct object_list {
	struct object *item;
	struct object_list *next;
};
struct object_refs {
	unsigned count;
	struct object *base;
	struct object *ref[FLEX_ARRAY]; /* more */
};
struct object_array {
	unsigned int nr;
	unsigned int alloc;
	struct object_array_entry {
		struct object *item;
		const char *name;
	} *objects;
};
#define TYPE_BITS   3
#define FLAG_BITS  27
/*
 * The object type is stored in 3 bits.
 */
enum object_type {
	OBJ_NONE = 0,
	OBJ_COMMIT = 1,
	OBJ_TREE = 2,
	OBJ_BLOB = 3,
	OBJ_TAG = 4,
	/* 5/6 for future expansion */
	OBJ_DELTA = 7,
	OBJ_BAD,
};
struct object {
	unsigned parsed : 1;
	unsigned used : 1;
	unsigned type : TYPE_BITS;
	unsigned flags : FLAG_BITS;
	unsigned char sha1[20];
};
extern int track_object_refs;
extern const char *type_names[9];
extern unsigned int get_max_object_index(void);
extern struct object *get_indexed_object(unsigned int);
static inline const char *typename(unsigned int type)
{
	return type_names[type > OBJ_BAD ? OBJ_BAD : type];
}
extern struct object_refs *lookup_object_refs(struct object *);
/** Internal only **/
struct object *lookup_object(const unsigned char *sha1);
/** Returns the object, having looked it up as being the given type. **/
struct object *lookup_object_type(const unsigned char *sha1, const char *type);
void created_object(const unsigned char *sha1, struct object *obj);
/** Returns the object, having parsed it to find out what it is. **/
struct object *parse_object(const unsigned char *sha1);
/** Returns the object, with potentially excess memory allocated. **/
struct object *lookup_unknown_object(const unsigned  char *sha1);
struct object_refs *alloc_object_refs(unsigned count);
void set_object_refs(struct object *obj, struct object_refs *refs);
void mark_reachable(struct object *obj, unsigned int mask);
struct object_list *object_list_insert(struct object *item, 
				       struct object_list **list_p);
void object_list_append(struct object *item,
			struct object_list **list_p);
unsigned object_list_length(struct object_list *list);
int object_list_contains(struct object_list *list, struct object *obj);
/* Object array handling .. */
void add_object_array(struct object *obj, const char *name, struct object_array *array);
#endif /* OBJECT_H */
