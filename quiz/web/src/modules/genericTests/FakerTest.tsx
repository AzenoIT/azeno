// eslint-disable-next-line import/no-extraneous-dependencies
import { faker } from "@faker-js/faker";
import type { SexType } from "@faker-js/faker";

type SubscriptionTier = "free" | "basic" | "pro";

class User {
    _id: string;

    avatar: string;

    birthday: Date;

    email: string;

    firstName: string;

    lastName: string;

    sex: SexType;

    subscriptionTier: SubscriptionTier;

    constructor(
        _id: string,
        avatar: string,
        birthday: Date,
        email: string,
        firstName: string,
        lastName: string,
        sex: SexType,
        subscriptionTier: SubscriptionTier
    ) {
        // eslint-disable-next-line no-underscore-dangle
        this._id = _id;
        this.avatar = avatar;
        this.birthday = birthday;
        this.email = email;
        this.firstName = firstName;
        this.lastName = lastName;
        this.sex = sex;
        this.subscriptionTier = subscriptionTier;
    }
}

function createRandomUser(): User {
    const sex = faker.name.sexType();
    const firstName = faker.name.firstName(sex);
    const lastName = faker.name.lastName();
    const email = faker.helpers.unique(faker.internet.email, [firstName, lastName]);

    return {
        _id: faker.datatype.uuid(),
        avatar: faker.image.avatar(),
        birthday: faker.date.birthdate(),
        email,
        firstName,
        lastName,
        sex,
        subscriptionTier: faker.helpers.arrayElement(["free", "basic", "pro"]),
    };
}

function FakerTest() {
    const user = createRandomUser();

    return <pre>{JSON.stringify(user)}</pre>;
}

export default FakerTest;
