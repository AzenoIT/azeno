// eslint-disable-next-line import/no-extraneous-dependencies
import { faker } from "@faker-js/faker";
import type { SexType } from "@faker-js/faker";

type SubscriptionTier = "free" | "basic" | "pro";

class User {
    // eslint-disable-next-line no-useless-constructor
    constructor(
        public _id: string,
        public avatar: string,
        public birthday: Date,
        public email: string,
        public firstName: string,
        public lastName: string,
        public sex: SexType,
        public subscriptionTier: SubscriptionTier
    ) {}
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
